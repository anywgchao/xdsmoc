'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 16:24:52
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-
# Browser
from xdsmoc.softwares.browsers.chromium_based import chromium_browsers
from xdsmoc.softwares.browsers.ie import IE
from xdsmoc.softwares.browsers.mozilla import firefox_browsers
from xdsmoc.softwares.browsers.ucbrowser import UCBrowser


def get_categories():
    category = {
        'browsers': {'help': 'Web browsers supported'},
    }
    return category


def get_modules():
    module_names = [
        IE(),
        UCBrowser()
    ]
    return module_names + chromium_browsers + firefox_browsers
