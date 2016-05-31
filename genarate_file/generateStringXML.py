#!/user/bin/python
# -*- coding: UTF-8 -*-
import sys
import generateXML

def alert():
	print("""
generateStringXML: generateStringXML <file> <new file> [split regular express].
The default split regular express is "="
The line that start with "#" will be ignored.
The result is like : 
	<string name="key">value</string>
""")

minParams = 3

def main(argv):
	global minParams
	tag = "string"
	if len(argv) < minParams:
		print("params length is " + str(len(argv)) + " and is less than " + str(minParams) )
		alert()
	elif len(argv) == minParams:
		path = argv[1]
		newPath = argv[2]
		regExpress = "="
		generateXML.main(["string",path,newPath,regExpress,tag])
	elif len(argv) == (minParams + 1):
		path = argv[1]
		newPath = argv[2]
		regExpress = argv[3]
		generateXML.main(["string",path,newPath,regExpress,tag])
	else:
		print("params length is " + str(len(argv)) + " and is more than 4.")
		alert()

if __name__ == '__main__':
	main(sys.argv)