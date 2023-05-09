'''
@Author: Daboluo
@Date: 2018-12-19 11:50:49
@LastEditTime: 2020-06-11 11:11:25
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

import re
try:
    import _winreg as winreg
    import chardet
except ImportError:
    import winreg

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo
from xdsmoc.config.winstructure import *
from xdsmoc.config.winstructure import Win32CryptUnprotectData


class OpenVPN(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(
            self, name='openvpn', category='vpn', registry_used=True, winapi_used=True)

    def check_openvpn_installed(self):
        try:
            key = OpenKey(HKEY_CURRENT_USER, 'Software\\OpenVPN-GUI\\Configs')
            return key
        except Exception as e:
            self.debug(str(e))
            return False

    def decrypt_password(self, encrypted_password, entropy):
        result_bytes = Win32CryptUnprotectData(encrypted_password,
                                               entropy=entropy,
                                               is_current_user=constant.is_current_user,
                                               user_dpapi=constant.user_dpapi)
        return result_bytes.decode("utf-8")

    def get_credentials(self, key):
        pwd_found = []
        num_profiles = winreg.QueryInfoKey(key)[0]
        for n in range(num_profiles):
            name_skey = winreg.EnumKey(key, n)
            skey = OpenKey(key, name_skey)
            values = {'Profile': name_skey}
            re_pattern = re.compile(
                u'[\u0000]', re.UNICODE)
            try:
                encrypted_password = winreg.QueryValueEx(skey, "auth-data")[0]
                encode_username = winreg.QueryValueEx(skey, "username")[0]
                entropy = winreg.QueryValueEx(skey, "entropy")[0][:-1]
                password = self.decrypt_password(encrypted_password, entropy)
                values['Username'] = re_pattern.sub(u'', encode_username.decode("utf-8"))
                values['Password'] = re_pattern.sub(u'', password)
            except Exception as e:
                self.debug(str(e))
            pwd_found.append(values)
            winreg.CloseKey(skey)
        winreg.CloseKey(key)

        return pwd_found

    def run(self):
        openvpn_key = self.check_openvpn_installed()
        if openvpn_key:
            results = self.get_credentials(openvpn_key)
            if results:
                return results
