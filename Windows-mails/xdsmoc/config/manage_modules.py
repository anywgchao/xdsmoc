'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 19:37:38
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

from xdsmoc.softwares.mails.outlook import Outlook
from xdsmoc.softwares.mails.thunderbird import Thunderbird


def get_categories():
    category = {
        'mails': {'help': 'Email clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # Mails
        Outlook(),
        Thunderbird(),
    ]
    return module_names
