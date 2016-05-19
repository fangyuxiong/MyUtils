#!/user/bin/python
# -*- coding: UTF-8 -*-
import sys
import generateFile

def alert():
	print("""
generateXML: generateXML <file> <new file> [split regular express] <tag>.
The default split regular express is "="
The line that start with "#" will be ignored.
The result is like : 
	<tag name="key">value</tag>
""")

minParams = 4

path = ""
newPath = ""
regExpress = "="
tag = ""

def analysisTag():
	if not tag.strip():
		print("tag is empty")
	left = "<" + tag + " name=\""
	middle = "\">"
	right = "</" + tag + ">"
	generateFile.main(["xml",path,newPath,regExpress,left,middle,right])

def main(argv):
	global minParams,path,newPath,regExpress,tag
	if len(argv) < minParams:
		print("params length is " + str(len(argv)) + " and is less than " + str(minParams) )
		alert()
	elif len(argv) == minParams:
		path = argv[1]
		newPath = argv[2]
		regExpress = "="
		tag = argv[3]
		analysisTag()
	elif len(argv) == (minParams + 1):
		path = argv[1]
		newPath = argv[2]
		regExpress = argv[3]
		tag = argv[4]
		analysisTag()
	else:
		print("params length is " + str(len(argv)) + " and is more than 5.")
		alert()

if __name__ == '__main__':
	main(sys.argv)