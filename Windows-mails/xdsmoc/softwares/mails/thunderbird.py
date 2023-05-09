# -*- coding: utf-8 -*-


import ctypes as ct
import json
import os
import sqlite3
import sys
from base64 import b64decode

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo

try:
    # Python 3
    from subprocess import DEVNULL
except ImportError:
    # Python 2
    DEVNULL = open(os.devnull, 'w')

try:
    # Python 3
    from urllib.parse import urlparse
except ImportError:
    # Python 2
    from urlparse import urlparse

try:
    # Python 3
    from configparser import ConfigParser
    raw_input = input
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser

PY3 = sys.version_info.major > 2
# Windows uses a mixture of different codecs for different components
# ANSI CP1252 for system messages, while NSS uses UTF-8
# To further complicate things, with python 2.7 the default stdout/stdin codec
# isn't UTF-8 but language dependent (tested on Windows 7)

if os.name == "nt":
    SYS_ENCODING = "cp1252"
    LIB_ENCODING = "utf8"
else:
    SYS_ENCODING = "utf8"
    LIB_ENCODING = "utf8"

# When using pipes stdin/stdout encoding may be None
USR_ENCODING = sys.stdin.encoding or sys.stdout.encoding or "utf8"


def py2_decode(_bytes, encoding=USR_ENCODING):
    if PY3:
        return _bytes
    else:
        return _bytes.decode(encoding)


def py2_encode(_unicode, encoding=USR_ENCODING):
    if PY3:
        return _unicode
    else:
        return _unicode.encode(encoding)


class NotFoundError(Exception):
    """Exception to handle situations where a credentials file is not found
    """
    pass


class Exit(Exception):
    """Exception to allow a clean exit from any point in execution
    """
    ERROR = 1
    MISSING_PROFILEINI = 2
    MISSING_SECRETS = 3
    BAD_PROFILEINI = 4
    LOCATION_NO_DIRECTORY = 5
    BAD_SECRETS = 6

    FAIL_LOCATE_NSS = 10
    FAIL_LOAD_NSS = 11
    FAIL_INIT_NSS = 12
    FAIL_NSS_KEYSLOT = 13
    FAIL_SHUTDOWN_NSS = 14
    BAD_MASTER_PASSWORD = 15
    NEED_MASTER_PASSWORD = 16

    PASSSTORE_NOT_INIT = 20
    PASSSTORE_MISSING = 21
    PASSSTORE_ERROR = 22

    READ_GOT_EOF = 30
    MISSING_CHOICE = 31
    NO_SUCH_PROFILE = 32

    UNKNOWN_ERROR = 100
    KEYBOARD_INTERRUPT = 102

    def __init__(self, exitcode):
        self.exitcode = exitcode

    def __unicode__(self):
        return "Premature program exit with exit code {0}".format(self.exitcode)


class Credentials(object):
    """Base credentials backend manager
    """

    def __init__(self, db):
        self.db = db
        if not os.path.isfile(db):
            raise NotFoundError("ERROR - {0} database not found\n".format(db))

    def __iter__(self):
        pass

    def done(self):
        """Override this method if the credentials subclass needs to do any
        action after interaction
        """
        pass


class SqliteCredentials(Credentials):
    """SQLite credentials backend manager
    """

    def __init__(self, profile):
        db = os.path.join(profile, "signons.sqlite")
        super(SqliteCredentials, self).__init__(db)
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def __iter__(self):
        self.c.execute("SELECT hostname, encryptedUsername, encryptedPassword, encType "
                       "FROM moz_logins")
        for i in self.c:
            # yields hostname, encryptedUsername, encryptedPassword, encType
            yield i

    def done(self):
        """Close the sqlite cursor and database connection
        """
        super(SqliteCredentials, self).done()
        self.c.close()
        self.conn.close()


class JsonCredentials(Credentials):
    """JSON credentials backend manager
    """

    def __init__(self, profile):
        db = os.path.join(profile, "logins.json")
        super(JsonCredentials, self).__init__(db)

    def __iter__(self):
        with open(self.db) as fh:
            data = json.load(fh)
            try:
                logins = data["logins"]
            except Exception:
                raise Exit(Exit.BAD_SECRETS)

            for i in logins:
                yield (i["hostname"], i["encryptedUsername"],
                       i["encryptedPassword"], i["encType"])


class NSSDecoder(object):
    class SECItem(ct.Structure):
        """struct needed to interact with libnss
        """
        _fields_ = [
            ('type', ct.c_uint),
            ('data', ct.c_char_p),  # actually: unsigned char *
            ('len', ct.c_uint),
        ]

    class PK11SlotInfo(ct.Structure):
        """opaque structure representing a logical PKCS slot
        """

    def __init__(self):
        # Locate libnss and try loading it
        self.NSS = None
        self.load_libnss()

        SlotInfoPtr = ct.POINTER(self.PK11SlotInfo)
        SECItemPtr = ct.POINTER(self.SECItem)

        self._set_ctypes(ct.c_int, "NSS_Init", ct.c_char_p)
        self._set_ctypes(ct.c_int, "NSS_Shutdown")
        self._set_ctypes(SlotInfoPtr, "PK11_GetInternalKeySlot")
        self._set_ctypes(None, "PK11_FreeSlot", SlotInfoPtr)
        self._set_ctypes(ct.c_int, "PK11_CheckUserPassword",
                         SlotInfoPtr, ct.c_char_p)
        self._set_ctypes(ct.c_int, "PK11SDR_Decrypt",
                         SECItemPtr, SECItemPtr, ct.c_void_p)
        self._set_ctypes(None, "SECITEM_ZfreeItem", SECItemPtr, ct.c_int)

        # for error handling
        self._set_ctypes(ct.c_int, "PORT_GetError")
        self._set_ctypes(ct.c_char_p, "PR_ErrorToName", ct.c_int)
        self._set_ctypes(ct.c_char_p, "PR_ErrorToString",
                         ct.c_int, ct.c_uint32)

    def _set_ctypes(self, restype, name, *argtypes):
        """Set input/output types on libnss C functions for automatic type casting
        """
        res = getattr(self.NSS, name)
        res.restype = restype
        res.argtypes = argtypes
        setattr(self, "_" + name, res)

    @staticmethod
    def find_nss(locations, nssname):
        """Locate nss is one of the many possible locations
        """
        fail_errors = []

        for loc in locations:
            nsslib = os.path.join(loc, nssname)
            if os.name == "nt":
                # On windows in order to find DLLs referenced by nss3.dll
                # we need to have those locations on PATH
                os.environ["PATH"] = ';'.join([loc, os.environ["PATH"]])
                # However this doesn't seem to work on all setups and needs to be
                # set before starting python so as a workaround we chdir to
                # Firefox's nss3.dll location
                if loc:
                    if not os.path.isdir(loc):
                        # No point in trying to load from paths that don't exist
                        continue

                    workdir = os.getcwd()
                    os.chdir(loc)

            try:
                nss = ct.CDLL(nsslib)
            except OSError as e:
                fail_errors.append((nsslib, str(e)))
            else:
                return nss
            finally:
                if os.name == "nt" and loc:
                    # Restore workdir changed above
                    os.chdir(workdir)

        else:
            raise Exit(Exit.FAIL_LOCATE_NSS)

    def load_libnss(self):
        """Load libnss into python using the CDLL interface
        """
        if os.name == "nt":
            nssname = "nss3.dll"
            locations = (
                "",  # Current directory or system lib finder
                r"C:\Program Files (x86)\Mozilla Firefox",
                r"C:\Program Files\Mozilla Firefox",
                r"C:\Program Files (x86)\Nightly",
                r"C:\Program Files\Nightly",
            )

        elif os.uname()[0] == "Darwin":
            nssname = "libnss3.dylib"
            locations = (
                "",  # Current directory or system lib finder
                "/usr/local/lib/nss",
                "/usr/local/lib",
                "/opt/local/lib/nss",
                "/sw/lib/firefox",
                "/sw/lib/mozilla",
                "/usr/local/opt/nss/lib",  # nss installed with Brew on Darwin
                "/opt/pkg/lib/nss",  # installed via pkgsrc
            )

        else:
            nssname = "libnss3.so"
            locations = (
                "",  # Current directory or system lib finder
                "/usr/lib",
                "/usr/lib32",
                "/usr/lib64",
                "/usr/lib/nss",
                "/usr/lib32/nss",
                "/usr/lib64/nss",
                "/usr/local/lib",
                "/usr/local/lib/nss",
                "/opt/local/lib",
                "/opt/local/lib/nss",
                os.path.expanduser("~/.nix-profile/lib"),
            )

        # If this succeeds libnss was loaded
        self.NSS = self.find_nss(locations, nssname)

    def handle_error(self):
        """If an error happens in libnss, handle it and print some debug information
        """
        code = self._PORT_GetError()
        name = self._PR_ErrorToName(code)
        name = "NULL" if name is None else name.decode(SYS_ENCODING)
        # 0 is the default language (localization related)
        text = self._PR_ErrorToString(code, 0)
        text = text.decode(SYS_ENCODING)

    def decode(self, data64):
        data = b64decode(data64)
        inp = self.SECItem(0, data, len(data))
        out = self.SECItem(0, None, 0)

        err = self._PK11SDR_Decrypt(inp, out, None)
        try:
            if err == -1:
                self.handle_error()
                raise Exit(Exit.NEED_MASTER_PASSWORD)
            res = ct.string_at(out.data, out.len).decode(LIB_ENCODING)
        finally:
            # Avoid leaking SECItem
            self._SECITEM_ZfreeItem(out, 0)

        return res


class NSSInteraction(object):
    """
    Interact with lib NSS
    """

    def __init__(self):
        self.profile = None
        self.NSS = NSSDecoder()

    def load_profile(self, profile):
        """Initialize the NSS library and profile
        """
        self.profile = profile
        profile = profile.encode(LIB_ENCODING)
        err = self.NSS._NSS_Init(b"sql:" + profile)

        if err != 0:
            self.NSS.handle_error()
            raise Exit(Exit.FAIL_INIT_NSS)

    def authenticate(self, interactive):
        """Check if the current profile is protected by a master password,
        prompt the user and unlock the profile.
        """
        keyslot = self.NSS._PK11_GetInternalKeySlot()
        if not keyslot:
            self.NSS.handle_error()
            raise Exit(Exit.FAIL_NSS_KEYSLOT)
        self.NSS._PK11_FreeSlot(keyslot)

    def unload_profile(self):
        """Shutdown NSS and deactive current profile
        """
        err = self.NSS._NSS_Shutdown()
        if err != 0:
            self.NSS.handle_error()
            raise Exit(Exit.FAIL_SHUTDOWN_NSS)

    def decode_entry(self, user64, passw64):
        """Decrypt one entry in the database
        """
        user = self.NSS.decode(user64)
        passw = self.NSS.decode(passw64)
        return user, passw

    def decrypt_passwords(self, export):
        pwd_found = []
        """
        Decrypt requested profile using the provided password and print out all
        stored passwords.
        """
        credentials = obtain_credentials(self.profile)
        to_export = {}

        for url, user, passw, enctype in credentials:
            # enctype informs if passwords are encrypted and protected by
            # a master password
            if enctype:
                user, passw = self.decode_entry(user, passw)

            if export:
                # Keep track of web-address, username and passwords
                # If more than one username exists for the same web-address
                # the username will be used as name of the file
                address = urlparse(url)
                if address.netloc not in to_export:
                    to_export[address.netloc] = {user: passw}
                else:
                    to_export[address.netloc][user] = passw

            url_sqplit = py2_encode(url, USR_ENCODING).split('://')
            pwd_found.append({
                "Type": url_sqplit[0],
                "Smtp": url_sqplit[1],
                "Username": "{0}".format(py2_encode(user, USR_ENCODING)),
                "Password": "{0}".format(py2_encode(passw, USR_ENCODING)),
            })
        return pwd_found


def obtain_credentials(profile):
    """Figure out which of the 2 possible backend credential engines is available
    """
    try:
        credentials = JsonCredentials(profile)
    except NotFoundError:
        try:
            credentials = SqliteCredentials(profile)
        except NotFoundError:
            raise Exit(Exit.MISSING_SECRETS)

    return credentials


def get_sections(profiles):
    """
    Returns hash of profile numbers and profile names.
    """
    sections = {}
    i = 1
    for section in profiles.sections():
        if section.startswith("Profile"):
            sections[str(i)] = profiles.get(section, "Path")
            i += 1
        else:
            continue
    return sections


def print_sections(sections, textIOWrapper=sys.stderr):
    """
    Prints all available sections to an textIOWrapper (defaults to sys.stderr)
    """
    for i in sorted(sections):
        textIOWrapper.write("{0} -> {1}\n".format(i, sections[i]))
    textIOWrapper.flush()


def ask_section(profiles, choice_arg):
    """
    Prompt the user which profile should be used for decryption
    """
    sections = get_sections(profiles)

    # Do not ask for choice if user already gave one
    if choice_arg and len(choice_arg) == 1:
        choice = choice_arg[0]
    else:
        # If only one menu entry exists, use it without prompting
        if len(sections) == 1:
            choice = "1"

        else:
            choice = None
            while choice not in sections:
                sys.stderr.write(
                    "Select the Firefox profile you wish to decrypt\n")
                print_sections(sections)
                try:
                    choice = raw_input()
                except EOFError:
                    raise Exit(Exit.READ_GOT_EOF)

    try:
        final_choice = sections[choice]
    except KeyError:
        raise Exit(Exit.NO_SUCH_PROFILE)

    return final_choice


def read_profiles(basepath):
    """
    Parse Firefox profiles in provided location.
    If list_profiles is true, will exit after listing available profiles.
    """
    profileini = os.path.join(basepath, "profiles.ini")
    if not os.path.isfile(profileini):
        raise Exit(Exit.MISSING_PROFILEINI)

    # Read profiles from Firefox profile folder
    profiles = ConfigParser()
    profiles.read(profileini)

    return profiles


def get_profile(basepath, interactive, choice):
    """
    Select profile to use by either reading profiles.ini or assuming given
    path is already a profile
    If interactive is false, will not try to ask which profile to decrypt.
    choice contains the choice the user gave us as an CLI arg.
    If list_profiles is true will exits after listing all available profiles.
    """
    try:
        profiles = read_profiles(basepath)
    except Exit as e:
        if e.exitcode == Exit.MISSING_PROFILEINI:
            profile = basepath

            if not os.path.isdir(profile):
                raise
        else:
            raise
    else:
        if not interactive:
            sections = get_sections(profiles)

            if choice and len(choice) == 1:
                try:
                    section = sections[(choice[0])]
                except KeyError:
                    raise Exit(Exit.NO_SUCH_PROFILE)

            elif len(sections) == 1:
                section = sections['1']

            else:
                raise Exit(Exit.MISSING_CHOICE)
        else:
            # Ask user which profile to open
            section = ask_section(profiles, choice)

        section = py2_decode(section, LIB_ENCODING)
        profile = os.path.join(basepath, section)

        if not os.path.isdir(profile):
            raise Exit(Exit.BAD_PROFILEINI)

    return profile


class Thunderbird(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'Thunderbird', 'mails')

    def run(self):
        # Initialize nss before asking the uspasser for input
        nss = NSSInteraction()
        profile_path = os.path.join(
            constant.profile['APPDATA'], u'Thunderbird')

        interactive = True
        choice = ""
        profile = get_profile(profile_path, interactive, choice)
        # Start NSS for selected profile
        nss.load_profile(profile)
        # Check if profile is password protected and prompt for a password
        nss.authenticate(interactive)
        # Decode all passwords
        export_pass = False
        pwd_found = nss.decrypt_passwords(export=export_pass)
        # And shutdown NSS
        nss.unload_profile()
        return pwd_found
