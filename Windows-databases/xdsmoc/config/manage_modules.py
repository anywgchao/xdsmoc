'''
@Author: Daboluo
@Date: 2019-11-19 15:29:21
@LastEditTime: 2020-06-10 19:57:57
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

# Databases
from xdsmoc.softwares.databases.dbvis import Dbvisualizer
from xdsmoc.softwares.databases.postgresql import PostgreSQL
from xdsmoc.softwares.databases.robomongo import Robomongo
from xdsmoc.softwares.databases.sqldeveloper import SQLDeveloper
from xdsmoc.softwares.databases.squirrel import Squirrel


def get_categories():
    category = {
        'databases': {'help': 'SQL/NoSQL clients supported'},
    }
    return category


def get_modules():
    module_names = [
        Dbvisualizer(),
        Squirrel(),
        SQLDeveloper(),
        Robomongo(),
        PostgreSQL(),
    ]
    return module_names
