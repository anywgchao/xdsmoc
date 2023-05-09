'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 20:10:44
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# system password
from xdsmoc.softwares.windows.autologon import Autologon
from xdsmoc.softwares.windows.cachedump import Cachedump
from xdsmoc.softwares.windows.credfiles import CredFiles
from xdsmoc.softwares.windows.credman import Credman
from xdsmoc.softwares.windows.hashdump import Hashdump
from xdsmoc.softwares.windows.lsa_secrets import LSASecrets
from xdsmoc.softwares.windows.ppypykatz import Pypykatz
from xdsmoc.softwares.windows.vault import Vault
from xdsmoc.softwares.windows.vaultfiles import VaultFiles
from xdsmoc.softwares.windows.windows import WindowsPassword


def get_categories():
    category = {
        'windows': {'help': 'Windows credentials (credential manager, etc.)'},
    }
    return category


def get_modules():
    module_names = [
        # Windows
        # Autologon(),
        # Pypykatz(),
        # Cachedump(),
        Credman(),
        # Hashdump(),
        # LSASecrets(),
        CredFiles(),
        Vault(),
        VaultFiles(),
        WindowsPassword(),
    ]
    return module_names
