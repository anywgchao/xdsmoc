# -*- coding: utf-8 -*-
import os
import struct

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo


class FtpNavigator(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'ftpnavigator', 'ftp')

    def decode(self, encode_password):
        password = ''
        for p in encode_password:
            password += chr(struct.unpack('B', p)[0] ^ 0x19)
        return password
    
    def run(self):
        paths = [
            os.path.join(constant.profile['HOMEDRIVE'], u'\\FTP Navigator', u'Ftplist.txt'),
            os.path.join(u'C:\\Program Files (x86)\\FTP Navigator', u'Ftplist.txt'),
            os.path.join(u'C:\\Program Files\\FTP Navigator', u'Ftplist.txt')
            ]
        elements = {'Name': 'Name', 'Server': 'Host',
                    'Port': 'Port', 'User': 'Login', 'Password': 'Password'}
        for path in paths:
            pwd_found = []
            if os.path.exists(path):
                with open(path, 'r') as f:
                    for ff in f:
                        values = {}
                        info = ff.split(';')
                        for i in info:
                            i = i.split('=')
                            for e in elements:
                                if i[0] == e:
                                    try:
                                        if i[0] == "Password" and i[1] != '1' and i[1] != '0':
                                            values['Password'] = self.decode(i[1])
                                        else:
                                            values[elements[i[0]]] = i[1]
                                    except:
                                        values['Password'] = i[1]
                        # used to save the password if it is an anonymous authentication
                        if values['Login'] == 'anonymous' and 'Password' not in values:
                            values['Password'] = 'anonymous'

                        pwd_found.append(values)

                return pwd_found
