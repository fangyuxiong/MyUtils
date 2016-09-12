#!/user/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import glob
import os
import sys
import re
from argv_engine import process_argv

vebose = True

saveToFile = False

saveFilename = "log"

openFile = None

keys=['-r','-v','-s','-f']

def countLines(dir,match):
	count = [0,0]
	compiler = None
	try:
		compiler = re.compile(match)
	except Exception, e:
		print "re.compile(" + match + ") failed."
		return None
	for fn in glob.glob(dir + os.sep + '*'):
		if os.path.isfile(fn):
			if not compiler.search(getFilename(fn)):
			 	continue
			num = readlines(fn)
			showLines(fn,num,True)
			addLines(count,num)
		else:
			addLines(count , countLines(fn,match))
	showLines(dir,count,False)
	return count

def getFilename(path):
	index = path.rfind(os.sep)
	name = ""
	if index < 0:
		name = path
	else:
		name = path[index+1 : ]
	return name

def addLines(old,new):
	old[0] += new[0]
	old[1] += new[1]

def readlines(filepath):
	f = open(filepath,'rU')
	lines = f.readlines()
	emptyLineNum = 0
	for l in lines:
		if isLineEmpty(l):
			emptyLineNum += 1
	l = len(lines)
	f.close()
	return [l,emptyLineNum]

def isLineEmpty(line):
	line = line.strip()
	empty = line == ""
	return empty

def showLines(fn,num,isfile):
	global vebose
	global saveToFile
	lines = num[0]
	emptyLines = num[1]
	reallyLine = lines - emptyLines
	ratio = 0
	if lines > 0:
		ratio = emptyLines / lines
	middle = " has "
	if not isfile:
		middle = " directory has "
	showStr = fn + middle + str(lines) + " lines. lines that contain really things : " + str(reallyLine) + " ; empty lines : " + str(emptyLines) + " ; empty line ratio : " + str(ratio) + " ."
	if vebose:
		print(showStr)
	if saveToFile:
		saveLog(showStr)

def saveLog(log):
	global openFile
	global saveFilename
	if openFile is None:
		openFile = open(saveFilename,'w')
	openFile.write(log+"\n")

def closeOpenFile():
	global openFile
	if openFile is not None:
		openFile.close()
	openFile = None

def stringIsEmpty(s):
	return s is None or s == ""

def isTrue(bool,defaultR = False):
	if bool is None or bool == "":
		return defaultR
	return bool == 't' or bool == 'T' or bool == 'true' or bool == 'True'

def how2Use():
	print '''python countLines.py <filepath> [options]
options:
	-r : regular expression for filename.
	-v : need vebose.
		t | T | true means True
	-s : need save log.
		t | T | true means True
	-f : log file name.
'''

def main():
	global vebose
	global saveToFile
	global saveFilename
	if len(sys.argv) < 2:
		how2Use()
		return -1
	arr = process_argv(sys.argv,keys,offset = 1)
	path = sys.argv[1]
	match = ".*"
	if arr is not None:
		if arr.has_key('-r'):
			match = arr['-r']
			if stringIsEmpty(match):
				match = "*"
		if arr.has_key('-v'):
			vebose = isTrue(arr['-v'],defaultR = True)
		if arr.has_key('-s'):
			saveToFile = isTrue(arr['-s'])
		if arr.has_key('-f'):
			tempF = arr['-f']
			if stringIsEmpty(tempF):
				tempF = saveFilename
			saveFilename = tempF
	countLines(path,match)
	closeOpenFile()

if __name__ == '__main__':
	main()

