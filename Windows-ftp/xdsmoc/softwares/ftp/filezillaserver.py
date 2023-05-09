'''
@Author: Daboluo
@Date: 2019-11-21 11:35:26
@LastEditTime: 2020-06-11 09:53:21
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-
import os
from xml.etree.cElementTree import ElementTree

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo


class FilezillaServer(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'filezillaserver', 'ftp')

    def run(self):
        path = os.path.join(constant.profile['APPDATA'], u'FileZilla Server')
        if os.path.exists(path):
            pwd_found = []
            file = u'FileZilla Server Interface.xml'

            xml_file = os.path.join(path, file)

            if os.path.exists(xml_file):
                tree = ElementTree(file=xml_file)
                root = tree.getroot()
                host = port = password = None

                for item in root.iter("Item"):
                    if item.attrib['name'] == 'Last Server Address':
                        host = item.text
                    elif item.attrib['name'] == 'Last Server Port':
                        port = item.text
                    elif item.attrib['name'] == 'Last Server Password':
                        password = item.text
                # if all((host, port, login)) does not work
                if host is not None and port is not None and password is not None:
                    pwd_found = [{
                        'Host': host,
                        'Port': port,
                        'Password': password,
                    }]

            return pwd_found