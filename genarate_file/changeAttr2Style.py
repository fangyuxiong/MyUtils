#!/user/bin/python
# -*- coding: UTF-8 -*-

# change 	"android:layout_width="wrap_content"" 
# to 		"<item name="android:layout_width">wrap_content</item>"

import os;
import sys;

LEFT = "<item name=\""
CENTER = "\">"
END = "</item>"

def changeString(src):
	if len(src) <= 0:
		return None
	src = deleteHead(src)
	src = src[0:len(src) - 1]
	key = src.split('="');
	return LEFT + key[0] + CENTER + key[1] + END;

def deleteHead(src):
	src = trim(src)
	i = src.find('android')
	if i == 0:
		return src
	i = src.find(':')
	return src[i + 1:len(src)]

def trim(src):
	return src.strip(' \t');

def changeEachLine(lines):
	result = []
	for line in lines.split('\n'):
		changed = changeString(line)
		if changed:
			result.append(changed)
	return result

def showEachLine(lines):
	for l in lines:
		if l:
			print str(l)

def main(argvs):
	print showEachLine(changeEachLine(argvs[1]))

if __name__ == '__main__':
	main(sys.argv)