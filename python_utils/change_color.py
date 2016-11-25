# -*- coding: UTF-8 -*-

import sys

def hex_to_rgb(hs):
	if start_with(hs,'0x') or start_with(hs,'0X'):
		hs = hs[2:]
	
	if len(hs) > 8 or len(hs) < 6:
		return None
	a = 0
	r = 0
	g = 0
	b = 0
	b = hexs_to_int(hs[-2:])
	g = hexs_to_int(hs[-4:-2])
	r = hexs_to_int(hs[-6:-4])
	if len(hs) == 7:
		a = hexs_to_int(hs[0:1])
	elif len(hs) == 8:
		a = hexs_to_int(hs[0:2])
	return [a,r,g,b]

def android_color_to_rgb(hs):
	hs = hs[1:]
	return hex_to_rgb(hs)

def start_with(s,reg):
	return s.find(reg) == 0

def hexs_to_int(hs):
	return int(hs,16)

def ints_to_hex(iss):
	return str(hex(int(iss)))[2:]

def argb_to_hex(rgb,array=False):
	argba = None
	if array:
		argba = rgb
	else:
		argba = rgb.split(',')
	l = len(argba)
	result = ""
	for x in range(0,l):
		result = result + ints_to_hex(argba[x])
	return result


def main():
	l = len(sys.argv)
	if l < 2:
		print '至少输入个数字啊！'
		return -1
	string = sys.argv[1]
	result = None
	if start_with(string,'#'):
		result = android_color_to_rgb(string)
	elif start_with(string,'0x') or start_with(string,'0X'):
		result = hex_to_rgb(string)
	elif string.find(',') >= 0:
		result = argb_to_hex(string)
	elif l > 2:
		result = argb_to_hex(sys.argv[1:l], array=True)
	if result is None:
		print "输入数字有误，可输入: 0x1af2dd; 0X1afada; '#ffabcd'; 123,234,233; 123 234 233"
		return -1
	print str(result)
	return result

if __name__ == '__main__':
	main()