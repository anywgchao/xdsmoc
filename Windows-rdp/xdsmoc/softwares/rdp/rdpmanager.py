'''
@Author: Daboluo
@Date: 2019-11-19 15:58:41
@LastEditTime: 2020-06-16 15:01:16
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-
import base64
import os
from xml.etree.cElementTree import ElementTree

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo
from xdsmoc.config.winstructure import Win32CryptUnprotectData


class RDPManager(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'rdpmanager', 'rdp', winapi_used=True)

    def decrypt_password(self, encrypted_password):
        try:
            decoded = base64.b64decode(encrypted_password)
            password_decrypted_bytes = Win32CryptUnprotectData(
                decoded, is_current_user=constant.is_current_user, user_dpapi=constant.user_dpapi)
            password_decrypted = password_decrypted_bytes.decode("utf-8")
            password_decrypted = password_decrypted.replace('\x00', '')
        except Exception:
            password_decrypted = encrypted_password.replace('\x00', '')
        return password_decrypted

    def format_output_tag(self, tag):
        tag = tag.lower()
        if 'username' in tag:
            tag = 'Login'
        elif 'hostname' in tag:
            tag = 'URL'
        return tag.capitalize()

    def check_tag_content(self, values, c):
        if 'password' in c.tag.lower():
            values['Password'] = self.decrypt_password(c.text)
        else:
            tag = self.format_output_tag(c.tag)
            values[tag] = c.text
        return values

    def parse_element(self, root, element):
        pwd_found = []
        try:
            for r in root.findall(element):
                values = {}
                for child in r.getchildren():
                    if child.tag == 'properties':
                        for c in child.getchildren():
                            values = self.check_tag_content(values, c)
                    elif child.tag == 'logonCredentials':
                        for c in child.getchildren():
                            values = self.check_tag_content(values, c)
                    else:
                        values = self.check_tag_content(values, child)

                if values:
                    pwd_found.append(values)
        except Exception as e:
            self.debug(str(e))

        return pwd_found

    def parse_xml(self, path, element):
        pwd_found = []
        tree = ElementTree(file=path)
        root = tree.getroot()
        try:
            for r in root.findall(element):
                values = {}
                for child in r.getchildren():
                    if child.tag == 'properties':
                        for c in child.getchildren():
                            values = self.check_tag_content(values, c)
                    elif child.tag == 'logonCredentials':
                        for c in child.getchildren():
                            values = self.check_tag_content(values, c)
                    else:
                        values = self.check_tag_content(values, child)
                if values:
                    pwd_found.append(values)
        except Exception as e:
            self.debug(str(e))

        return pwd_found

    def run(self):
        settings = [
            os.path.join(constant.profile['LOCALAPPDATA'],
                         u'Microsoft Corporation\\Remote Desktop Connection Manager\\RDCMan.settings'),
            os.path.join(constant.profile['LOCALAPPDATA'],
                         u'Microsoft\\Remote Desktop Connection Manager\\RDCMan.settings')
        ]

        for setting in settings:
            if os.path.exists(setting):
                self.debug(
                    u'Setting file found: {setting}'.format(setting=setting))

                tree = ElementTree(file=setting)
                root = tree.getroot()
                pwd_found = []

                elements = [
                    'CredentialsProfiles/credentialsProfiles/credentialsProfile',
                    'DefaultGroupSettings/defaultSettings/logonCredentials',
                    'DefaultGroupSettings/defaultSettings/properties',
                    'file/server'
                ]

                for element in elements:
                    pwd_found += self.parse_element(root, element)

                try:
                    for r in root.find('FilesToOpen'):
                        if os.path.exists(r.text):
                            elements = [
                                'file/server'
                            ]
                            self.debug(u'New setting file found: %s' % r.text)
                            for element in elements:
                                pwd_found += self.parse_xml(r.text, element)
                except Exception:
                    pass

                return pwd_found
