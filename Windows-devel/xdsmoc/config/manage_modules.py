'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-11 11:32:44
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

from xdsmoc.softwares.git.gitforwindows import GitForWindows
from xdsmoc.softwares.maven.mavenrepositories import MavenRepositories
# devel
from xdsmoc.softwares.svn.tortoise import Tortoise


def get_categories():
    category = {
        'devel': {'help': 'devel clients supported'},
    }
    return category


def get_modules():
    module_names = [
        # Git
        GitForWindows(),
        # Maven
        MavenRepositories(),
        # SVN
        Tortoise(),
    ]
    return module_names
