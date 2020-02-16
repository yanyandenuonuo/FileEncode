#!/usr/bin/python  
# -*- coding: utf-8 -*-

import os
import chardet


def show_encode(dir_path):
    paths = os.listdir(dir_path)
    for path in paths:
        # path = dir_path + '/' + path
        if os.path.isdir(dir_path + '/' + path):
            if path[0] != '.':
                show_encode(dir_path + '/' + path)
        else:
            path = dir_path + '/' + path
            file = open(path, 'r')
            data = file.read()
            file_encoding = chardet.detect(data)['encoding']
            if file_encoding != 'utf-8':
                print(str(path) + ': ' + str(file_encoding))


show_encode('E:/Project/Python')
