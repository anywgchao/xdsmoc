'''
@Author: Daboluo
@Date: 2019-11-21 12:57:06
@LastEditTime: 2020-06-10 19:44:04
@LastEditors: Do not edit
'''
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

if __name__ == '__main__':
    # Parse Arguments
    dist_path = './dist'
    build_path = './build'
    if os.path.isdir(dist_path) and os.path.isdir(build_path):
        shutil.rmtree(dist_path)
        shutil.rmtree(build_path)
    xd_cmd = 'pyinstaller -F xdsmoc-mails.py --upx-dir ./upx-3.95-win64 --icon ./icon/mails.ico'
    subprocess.Popen(xd_cmd, shell=True)