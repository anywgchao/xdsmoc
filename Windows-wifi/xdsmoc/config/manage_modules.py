'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 14:41:19
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# WIFI password
from xdsmoc.softwares.wifi.wifi import Wifi


def get_categories():
    category = {
        'wifi': {'help': 'Wifi'},
    }
    return category


def get_modules():
    module_names = [
        # Wifi
        Wifi()
    ]
    return module_names
