# -*- coding: utf-8 -*-

# Browsers
from xdsmoc.softwares.browsers.chromium_based import chromium_browsers
from xdsmoc.softwares.browsers.ie import IE
from xdsmoc.softwares.browsers.mozilla import firefox_browsers
from xdsmoc.softwares.browsers.ucbrowser import UCBrowser

# Chats
from xdsmoc.softwares.chats.pidgin import Pidgin
from xdsmoc.softwares.chats.psi import PSI
from xdsmoc.softwares.chats.skype import Skype


# Databases
from xdsmoc.softwares.databases.dbvis import Dbvisualizer
from xdsmoc.softwares.databases.postgresql import PostgreSQL
from xdsmoc.softwares.databases.robomongo import Robomongo
from xdsmoc.softwares.databases.sqldeveloper import SQLDeveloper
from xdsmoc.softwares.databases.squirrel import Squirrel
# Games
from xdsmoc.softwares.games.galconfusion import GalconFusion
from xdsmoc.softwares.games.kalypsomedia import KalypsoMedia
from xdsmoc.softwares.games.roguestale import RoguesTale
from xdsmoc.softwares.games.turba import Turba
# Git
from xdsmoc.softwares.git.gitforwindows import GitForWindows
# Mails
from xdsmoc.softwares.mails.outlook import Outlook
from xdsmoc.softwares.mails.thunderbird import Thunderbird
# Maven
from xdsmoc.softwares.maven.mavenrepositories import MavenRepositories
# Memory
from xdsmoc.softwares.memory.keepass import Keepass
from xdsmoc.softwares.memory.memorydump import MemoryDump
# Php
from xdsmoc.softwares.php.composer import Composer
# Svn
from xdsmoc.softwares.svn.tortoise import Tortoise
# Sysadmin
from xdsmoc.softwares.sysadmin.apachedirectorystudio import ApacheDirectoryStudio
from xdsmoc.softwares.sysadmin.coreftp import CoreFTP
from xdsmoc.softwares.sysadmin.cyberduck import Cyberduck
from xdsmoc.softwares.sysadmin.filezilla import Filezilla
from xdsmoc.softwares.sysadmin.ftpnavigator import FtpNavigator
from xdsmoc.softwares.sysadmin.opensshforwindows import OpenSSHForWindows
from xdsmoc.softwares.sysadmin.openvpn import OpenVPN
from xdsmoc.softwares.sysadmin.puttycm import Puttycm
from xdsmoc.softwares.sysadmin.rdpmanager import RDPManager
from xdsmoc.softwares.sysadmin.unattended import Unattended
from xdsmoc.softwares.sysadmin.vnc import Vnc
from xdsmoc.softwares.sysadmin.winscp import WinSCP
from xdsmoc.softwares.sysadmin.wsl import Wsl

# Wifi
from xdsmoc.softwares.wifi.wifi import Wifi

# Windows
from xdsmoc.softwares.windows.autologon import Autologon
from xdsmoc.softwares.windows.cachedump import Cachedump
from xdsmoc.softwares.windows.credman import Credman
from xdsmoc.softwares.windows.credfiles import CredFiles
from xdsmoc.softwares.windows.hashdump import Hashdump
from xdsmoc.softwares.windows.ppypykatz import Pypykatz
from xdsmoc.softwares.windows.lsa_secrets import LSASecrets
from xdsmoc.softwares.windows.vault import Vault
from xdsmoc.softwares.windows.vaultfiles import VaultFiles
from xdsmoc.softwares.windows.windows import WindowsPassword


def get_categories():
    category = {
        'browsers': {'help': 'Web browsers supported'},
        'chats': {'help': 'Chat clients supported'},
        'databases': {'help': 'SQL/NoSQL clients supported'},
        'games': {'help': 'Games etc.'},
        'git': {'help': 'GIT clients supported'},
        'mails': {'help': 'Email clients supported'},
        'maven': {'help': 'Maven java build tool'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'php': {'help': 'PHP build tool'},
        'svn': {'help': 'SVN clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'windows': {'help': 'Windows credentials (credential manager, etc.)'},
        'wifi': {'help': 'Wifi'},
    }
    return category


def get_modules():
    module_names = [
        # Browser
        IE(),
        UCBrowser(),

        # Chats
        Pidgin(),
        Skype(),
        PSI(),

        # Databases
        Dbvisualizer(),
        Squirrel(),
        SQLDeveloper(),
        Robomongo(),
        PostgreSQL(),

        # games
        KalypsoMedia(),
        GalconFusion(),
        RoguesTale(),
        Turba(),

        # Git
        GitForWindows(),

        # Mails
        Outlook(),
        Thunderbird(),

        # Maven
        MavenRepositories(),
        # Memory
        MemoryDump(),  # retrieve browsers and keepass passwords
        Keepass(),  # should be launched after memory dump

        # Php
        Composer(),

        # SVN
        Tortoise(),

        # Sysadmin
        ApacheDirectoryStudio(),
        CoreFTP(),
        Cyberduck(),
        Filezilla(),
        FtpNavigator(),
        Puttycm(),
        OpenSSHForWindows(),
        OpenVPN(),
        RDPManager(),
        Unattended(),
        WinSCP(),
        Vnc(),
        Wsl(),

        # Wifi
        Wifi(),

        # Windows
        Autologon(),
        Pypykatz(),
        Cachedump(),
        Credman(),
        Hashdump(),
        LSASecrets(),
        CredFiles(),
        Vault(),
        VaultFiles(),
        WindowsPassword()

    ]
    return module_names + chromium_browsers + firefox_browsers
