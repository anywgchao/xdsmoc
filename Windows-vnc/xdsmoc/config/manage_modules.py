'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 10:19:10
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# vnc
from xdsmoc.softwares.vnc.vnc import Vnc


def get_categories():
    category = {
        'vnc': {'help': 'vnc clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # vnc
        Vnc(),
    ]
    return module_names
