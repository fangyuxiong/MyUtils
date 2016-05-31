#!/user/bin/python
# -*- coding: UTF-8 -*-
import glob
import os
import sys
import re

def countLines(dir,match):
	count = 0
	for fn in glob.glob(dir + os.sep + '*'):
		print(fn)
		if os.path.isfile(fn):
			if not re.compile(match).search(fn):
			 	continue
			len = readlines(fn)
			print(fn+" has "+str(len)+" lines.")
			count = count + len
		else:
			count = count + countLines(fn,match)
	print(dir+" directory has "+str(count)+" lines.")
	return count	

def readlines(filepath):
	f = open(filepath,'rU')
	l = len(f.readlines())
	f.close()
	return l

if __name__ == '__main__':
	dir = sys.argv[1]
	match = sys.argv[2]
	f=open('log','w')
	old=sys.stdout #将当前系统输出储存到一个临时变量中
	sys.stdout=f  #输出重定向到文件
	countLines(dir,match)
	sys.stdout=old #还原原系统输出
	f.close() 
