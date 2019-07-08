# -*- coding: utf-8 -*-

# Browsers
from xdsmoc.softwares.browsers.chromium_based import chromium_browsers
from xdsmoc.softwares.browsers.ie import IE
from xdsmoc.softwares.browsers.mozilla import firefox_browsers
from xdsmoc.softwares.browsers.ucbrowser import UCBrowser


def get_categories():
    category = {
        'browsers': {'help': 'Web browsers supported'}
    }
    return category


def get_modules():
    module_names = [
        # Browser
        IE(),
        UCBrowser()
    ]
    return module_names + chromium_browsers + firefox_browsers
