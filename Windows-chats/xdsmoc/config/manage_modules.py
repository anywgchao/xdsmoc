'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 17:57:37
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# chats
from xdsmoc.softwares.chats.pidgin import Pidgin
from xdsmoc.softwares.chats.psi import PSI
from xdsmoc.softwares.chats.skype import Skype


def get_categories():
    category = {
        'chats': {'help': 'Chat clients supported'},
    }
    return category


def get_modules():
    module_names = [
        Pidgin(),
        Skype(),
        PSI(),
    ]
    return module_names
