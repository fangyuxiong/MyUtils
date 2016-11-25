# -*- coding: UTF-8 -*-

import sys

def main():
	if len(sys.argv) != 2:
		return -1
	a = float(sys.argv[1])
	ia = int(a * 255)
	print "十进制："+str(ia)
	print "十六进制："+str(hex(ia))

if __name__ == '__main__':
	main()