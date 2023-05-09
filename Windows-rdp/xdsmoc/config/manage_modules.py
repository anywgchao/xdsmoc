'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 11:22:46
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# rdp
from xdsmoc.softwares.rdp.rdpmanager import RDPManager


def get_categories():
    category = {
        'rdp': {'help': 'rdp clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # rdp
        RDPManager(),
    ]
    return module_names
