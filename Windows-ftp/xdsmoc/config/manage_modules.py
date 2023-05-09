'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 09:51:09
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# ftp
from xdsmoc.softwares.ftp.coreftp import CoreFTP
from xdsmoc.softwares.ftp.cyberduck import Cyberduck
from xdsmoc.softwares.ftp.filezilla import Filezilla
from xdsmoc.softwares.ftp.filezillaserver import FilezillaServer
from xdsmoc.softwares.ftp.ftpnavigator import FtpNavigator


def get_categories():
    category = {
        'ftp': {'help': 'FTP/FTPS clients supported'},
    }
    return category


def get_modules():
    module_names = [
        CoreFTP(),
        Cyberduck(),
        Filezilla(),
        FilezillaServer(),
        FtpNavigator()
    ]
    return module_names
