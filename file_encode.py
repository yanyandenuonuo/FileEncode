#!/usr/bin/python  
# -*- coding: utf-8 -*-

import os
import chardet

def show_encode(dir):
	paths = os.listdir(dir)
	for path in paths:
		# path = dir + '/' + path
		if(os.path.isdir(dir + '/' + path)):
			if(path[0] != '.'):
				show_encode(dir + '/' + path)
		else:
			path = dir + '/' + path
			file = open(path, 'r')
			data = file.read()
			file_encoding = chardet.detect(data)['encoding']
			if(file_encoding != 'utf-8'):
				print(str(path) + ': ' + str(file_encoding))

show_encode('E:/Project/PHP/UED')
