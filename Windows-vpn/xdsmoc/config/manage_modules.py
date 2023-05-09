'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 11:09:27
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# vpn
from xdsmoc.softwares.vpn.openvpn import OpenVPN


def get_categories():
    category = {
        'vpn': {'help': 'vpn clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # vpn
        OpenVPN(),
    ]
    return module_names
