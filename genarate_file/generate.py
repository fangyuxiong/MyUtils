#!/user/bin/python
# -*- coding: UTF-8 -*-
import sys
import os

def alert():
	print("""
generate: generate <file> <new file> [split regular express] <left> <middle> <right>.
The default split regular express is "="
The line that start with "#" will be ignored.
""")

minParams = 6

path = ""
newPath = ""
regExpress = "="
left = ""
middle = ""
right = ""
newFile = None

# 检查每行是否是#开头，是则返回0，不是返回-1
def checkAnnotation(line):
	return line.find("#",0,1);

def changeLine(line):
	if not line.strip():
		return "";
	li = line.split(regExpress,1)
	key = li[0]
	val = li[1].strip('\n')
	newLine = left + key + middle + val + right
	return newLine

def saveLine(line):
	global newFile
	if newFile == None:
		newFile = open(newPath,'a')
	newFile.write(line + '\n')

def readFile():
	global newFile
	# print(newFile)
	f = open(path,'r')
	for line in f:
		a = checkAnnotation(line)
		if a == 0:
			continue

		newLine = changeLine(line)
		if not newLine.strip():
			continue
		saveLine(newLine)
	newFile.close()
	f.close()

def doGenerate():
	if not path.strip():
		print("file path is empty")
		return -1
	if not regExpress.strip():
		print("split regular express is empty")
		return -1
	if not newPath.strip():
		print("generate file path is empty")
		return -1
	if not os.path.isfile(path):
		print("file is not found")
		return -1
	readFile()

def main(argv):
	global minParams,path,newPath,regExpress,left,middle,right
	if len(argv) < minParams:
		print("params length is " + str(len(argv)) + " and is less than " + str(minParams) )
		alert()
	elif len(argv) == minParams:
		path = argv[1]
		newPath = argv[2]
		regExpress = '='
		left = argv[3]
		middle = argv[4]
		right = argv[5]
		# print("without regular express")
		doGenerate()
	elif len(argv) == 7:
		path = argv[1]
		newPath = argv[2]
		regExpress = argv[3]
		left = argv[4]
		middle = argv[5]
		right = argv[6]
		# print("with regular express")
		doGenerate()
	else:
		print("params length is " + str(len(argv)) + " and is more than 7.")
		alert()

if __name__ == '__main__':
	main(sys.argv)
