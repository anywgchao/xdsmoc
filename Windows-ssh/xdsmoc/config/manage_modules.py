'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 11:02:58
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# ssh
from xdsmoc.softwares.ssh.opensshforwindows import OpenSSHForWindows
from xdsmoc.softwares.ssh.puttycm import Puttycm
from xdsmoc.softwares.ssh.winscp import WinSCP


def get_categories():
    category = {
        'ssh': {'help': 'ssh clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # vnc
        Puttycm(),
        OpenSSHForWindows(),
        WinSCP(),
    ]
    return module_names
