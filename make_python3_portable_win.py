# -*- coding: utf-8 -*-

import os
import re
import sys


# replace binary bytes
def execute_binary(file_name):
    # print(file_name)
    with open(file_name, 'rb') as rf:
        data = rf.read()
        # Delete the absolute path information, only remain python.exe
        data = re.sub(b'#!(.*?)python.exe', b'#!python.exe', data)
    with open(file_name, 'wb') as wf:
        wf.write(data)


# List all files in a directory, including sub dir
def get_file_list(target_dir, file_list):
    if os.path.isfile(target_dir):
        file_list.append(target_dir)
    elif os.path.isdir(target_dir):
        for s in os.listdir(target_dir):
            new_dir = os.path.join(target_dir, s)
            get_file_list(new_dir, file_list)
    return file_list


if __name__ == "__main__":

    print('Start making Python portable.')
    print('')

    # get current path
    if getattr(sys, 'frozen', False):
        root_dir = os.path.dirname(sys.executable)
    else:
        root_dir = os.path.dirname(os.path.abspath(__file__))

    files = get_file_list(root_dir, [])  # List all files in a directory, including sub dir
    for file in files:
        # modify exe files to be portable, excluding itself
        if file.endswith(r'.exe') and not file == os.path.join(root_dir, sys.executable):
            print("Modifying", file)
            path = os.path.join(root_dir, file)
            execute_binary(path)

    print('')
    print('Finish making Python portable.')
    print('You should run this program again after installing new module(s) for Python.')
    print('Press Enter to quit.')
    input()
