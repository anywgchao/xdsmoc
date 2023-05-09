'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 21:45:09
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

from xdsmoc.softwares.memory.keepass import Keepass
from xdsmoc.softwares.memory.memorydump import MemoryDump


def get_categories():
    category = {
        'memory': {'help': 'Retrieve passwords from memory'},
    }
    return category


def get_modules():
    module_names = [
        # Memory
        MemoryDump(),  # retrieve browsers and keepass passwords
        Keepass(),  # should be launched after memory dump
    ]
    return module_names
