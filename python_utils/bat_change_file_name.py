# -*- coding: UTF-8 -*-

import re
import os
import sys
import glob
from argv_engine import process_argv

keys=['-p','-r','-n']

# 旧名称, 关键字, 新名称
def change_name(old,reg,new):
	if old.find(reg) != -1:
		old = re.sub(reg,new,old)
	return old

def list_files_and_change(path,reg,new):
	for fn in glob.glob(path + os.sep + '*'):
		if os.path.isfile(fn):
			parent = get_file_parent_path(fn)
			old = get_filename(fn)
			new_name = change_name(old,reg,new)
			if parent is not None:
				new_name = parent + os.sep + new_name
			os.rename(fn,new_name)

def get_file_parent_path(path):
	index = path.rfind(os.sep)
	if index < 0:
		return None
	return path[0:index]

def get_filename(path):
	index = path.rfind(os.sep)
	name = ""
	if index < 0:
		name = path
	else:
		name = path[index+1 : ]
	return name

def how2Use():
	print '''python bat_change_file_name.py <options>
options:
	-p : path of direcotry that contain files to change name.
	-r : old string that need to replace.
	-n : new string to replace the old
'''

def main():
	if len(sys.argv) != 7:
		how2Use()
		return -1
	arr = process_argv(sys.argv,keys)
	path = arr['-p']
	reg = arr['-r']
	new_string = arr['-n']
	list_files_and_change(path,reg,new_string)

if __name__ == '__main__':
	main()





