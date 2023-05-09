'''
@Author: Daboluo
@Date: 2019-11-19 16:02:15
@LastEditTime: 2020-06-11 09:53:02
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-
import base64
import os
from xml.etree.cElementTree import ElementTree

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo


class Filezilla(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'filezilla', 'ftp')

    def run(self):
        path = os.path.join(constant.profile['APPDATA'], u'FileZilla')
        if os.path.exists(path):
            pwd_found = []
            for file in [u'sitemanager.xml', u'recentservers.xml', u'filezilla.xml']:

                xml_file = os.path.join(path, file)
                if os.path.exists(xml_file):
                    tree = ElementTree(file=xml_file)
                    if tree.findall('Servers/Server'):
                        servers = tree.findall('Servers/Server')
                    else:
                        servers = tree.findall('RecentServers/Server')

                    for server in servers:
                        host = server.find('Host')
                        port = server.find('Port')
                        login = server.find('User')
                        cname = server.find('Name')
                        password = server.find('Pass')

                        # if all((host, port, login)) does not work
                        if host is not None and port is not None and login is not None:
                            values = {
                                'ConnName': cname.text,
                                'Host': host.text,
                                'Port': port.text,
                                'Login': login.text,
                            }

                        if password is not None:
                            if 'encoding' in password.attrib and password.attrib['encoding'] == 'base64':
                                values['Password'] = base64.b64decode(
                                    password.text)
                            else:
                                values['Password'] = password.text

                        if values:
                            pwd_found.append(values)

            return pwd_found