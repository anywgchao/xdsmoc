# -*- coding: utf-8 -*-

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>                           Copyright © xdsmoc                             <
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
import os
import sys
import argparse
from encrypt_file import Aescrypt

"""
def output(output_dir=None, json_format=False):
    if output_dir:
        if os.path.isdir(output_dir):
            constant.folder_name = output_dir
        else:
            print('[!] Specify a directory, not a file !')

    if json_format:
        constant.output = 'json'

    if constant.output:
        if not os.path.exists(constant.folder_name):
            os.makedirs(constant.folder_name)
            constant.file_name_results = 'credentials'  # choice of the name to the user
        if constant.output != 'json':
            constant.st.write_header()
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='decrypt_file', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-version', action='version', version='Version_v1.1',
                        help='Show Version')
    parser.add_argument('-i', dest='source_file', action='store',
                        help='chose source file')
    parser.add_argument('-o', dest='target_file', action='store',
                        help='chose target file')
    parser.add_argument('-p', dest='password', action='store', default=None,
                        help='Add the secret key')
    # ------------------------------------------- Parse arguments -------------------------------------------
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = dict(parser.parse_args()._get_kwargs())
    source_file = args.get("source_file")
    target_file = args.get("target_file")
    try:
        if os.path.isfile(source_file):
            aescryptor = Aescrypt(args.get("password"))
            # file path
            decryption_text = aescryptor.decrypt_file(source_file, target_file)
        else:
            print('Source File Not Found')
    except Exception as e:
        print('error: {}'.format(e))
