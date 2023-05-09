'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 11:58:23
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# passtools
from xdsmoc.softwares.passtools.keepassconfig import KeePassConfig


def get_categories():
    category = {
        'passtools': {'help': 'passtools clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # vnc
        KeePassConfig(),
    ]
    return module_names
