# -*- coding: utf-8 -*-

import os
import json

from xdsmoc.config.constant import constant
from xdsmoc.config.module_info import ModuleInfo


class Robomongo(ModuleInfo):

    def __init__(self):
        ModuleInfo.__init__(self, 'robomongo', 'databases')

    def read_file_content(self, file_path):
        """
        Read the content of a file

        :param file_path: Path of the file to read.

        :return: File content as string.
        """
        content = ""
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file_handle:
                content = file_handle.read()

        return content

    def parse_json(self, connection_file_path):
        repos_creds = []
        with open(connection_file_path) as connection_file:
            try:
                connections_infos = json.load(connection_file)
            except Exception:
                return repos_creds

            for connection in connections_infos.get("connections", []):
                try:
                    creds = {
                        "Name": connection["connectionName"],
                        "Host": connection["serverHost"],
                        "Port": connection["serverPort"]
                    }
                    crd = connection["credentials"][0]
                    if crd.get("enabled"):
                        creds.update({
                            "AuthMode": "CREDENTIALS",
                            "DatabaseName": crd["databaseName"],
                            "AuthMechanism": crd["mechanism"],
                            "Login": crd["userName"],
                            "Password": crd["userPassword"]
                        })
                    else:
                        creds.update({
                            "Host": connection["ssh"]["host"],
                            "Port": connection["ssh"]["port"],
                            "Login": connection["ssh"]["userName"]
                        })
                        if connection["ssh"]["enabled"] and connection["ssh"]["method"] == "password":
                            creds.update({
                                "AuthMode": "SSH_CREDENTIALS",
                                "Password": connection["ssh"]["userPassword"]
                            })
                        else:
                            creds.update({
                                "AuthMode": "SSH_PRIVATE_KEY",
                                "Passphrase": connection["ssh"]["passphrase"],
                                "PrivateKey": self.read_file_content(connection["ssh"]["privateKeyFile"]),
                                "PublicKey": self.read_file_content(connection["ssh"]["publicKeyFile"])
                            })
                    repos_creds.append(creds)
                except Exception as e:
                    self.error(u"Cannot retrieve connections credentials '{error}'".format(error=e))
        return repos_creds

    def find_file(self, dpath, name):
        for relpath, dirs, files in os.walk(dpath):
            if name in files:
                full_path = os.path.join(dpath, relpath, name)
                return os.path.normpath(os.path.abspath(full_path))

    def run(self):
        """
        Extract all connection's credentials.
        :return: List of dict in which one dict contains all information for a connection.
        """
        # Name, path or a list of paths
        robomongo_path = [
            ".3T/robo-3t",
            ".config/robomongo"
        ]
        robomongo_name = [
            "robo3t.json",
            "robomongo.json"
        ]

        pwd_found = []
        for directory in robomongo_path:
            connection_path = os.path.join(constant.profile['USERPROFILE'],
                                           directory)
            if os.path.exists(connection_path):
                mongo_name_list = robomongo_name
                for mongo_name in mongo_name_list:
                    connection_file_path = self.find_file(connection_path, mongo_name)
                    try:
                        if os.path.exists(connection_file_path):
                            pwd_found = self.parse_json(connection_file_path)
                    except Exception as e:
                        pass
        return pwd_found
