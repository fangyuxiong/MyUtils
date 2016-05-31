#coding=utf-8

import os
import sys
import glob
from generateDrawables import main
from generateDrawables import IMAGE_PATH_EXTRA
from generateDrawables import IMAGE_OUTPATH_EXTRA
from generateDrawables import IMAGE_OUTNAME_EXTRA
from generateDrawables import IMAGE_MAX_SCALE
from generateDrawables import IMAGE_MIN_SCALE
from generateDrawables import IMAGE_MAX_SIZE 
from generateDrawables import DRAWABLE
from generateDrawables import MIPMAP
sys.path.append('/Users/XK/Desktop/MyUtils/python_utils')
from argv_engine import process_argv

PNG = '.png'

image_type = [PNG,'.jpg','.jpeg']

IC_LAUNCHER = '-ic'

def getNameByRes(res):
	name = os.path.split(res)[1]
	suffix = os.path.splitext(res)[1]
	if suffix != PNG:
		l = len(suffix)
		if l > 0:
			l = -l
		else:
			l = len(name)
		name = name[0:l]
		return name+PNG
	return name


def batchGenerateDrawables(res,out,child=DRAWABLE,name=None,ms=None,ass='xxx',iss='l'):
	if os.path.isfile(res):
		arr = ['generateDrawables.py',IMAGE_PATH_EXTRA,res,IMAGE_OUTPATH_EXTRA,out+os.sep+child]
		if name:
			name = getNameByRes(name)
		else:
			name = getNameByRes(res)
		arr.append(IMAGE_OUTNAME_EXTRA)
		arr.append(name)
		if ass:
			arr.append(IMAGE_MAX_SCALE)
			arr.append(ass)
		if iss:
			arr.append(IMAGE_MIN_SCALE)
			arr.append(iss)
		if ms:
			arr.append(IMAGE_MAX_SIZE)
			arr.append(ms)
		print_arr(arr)
		main(arr)
	if os.path.isdir(res):
		for suffix in image_type:
			for x in glob.glob(res + os.sep + '*' + suffix):
				batchGenerateDrawables(x,out,child=child,name=name,ms=ms,ass=ass,iss=iss)

def print_arr(arr):
	s = 'do '
	for x in xrange(0,len(arr)):
		s = s + arr[x] + ' '
	print s

def error():
	print """useage: python batchGenerateDrawables.py <pic dir | pic file> <out dir> [-extra argv]
extra:
	-ic : if set 'true' , the max size will be set to (192,192).
	-ms : the max size of output image,if not set, use the old image size.
		eg:	100-100
	-as : the max scale of image
		xxx | xx | x | h | m | l
		if not set, the max scale is "xxx".
	-is : the min scale of image 
		xxx | xx | x | h | m | l
		if not set, the min scale is "l"."""

def domain(argv):
	l = len(argv)
	if l < 3:
		error()
		return -1
	arr = process_argv(argv,[IC_LAUNCHER,IMAGE_MAX_SIZE,IMAGE_MAX_SCALE,IMAGE_MIN_SCALE],2)
	if IC_LAUNCHER in arr and arr[IC_LAUNCHER] == 'true':
		arr[IMAGE_MAX_SIZE] = '192-192'
	ms = None
	if IMAGE_MAX_SIZE in arr:
		ms = arr[IMAGE_MAX_SIZE]
	ass = 'xxx'
	if IMAGE_MAX_SCALE in arr:
		ass = arr[IMAGE_MAX_SCALE]
	iss = 'l'
	if IMAGE_MIN_SCALE in arr:
		iss = arr[IMAGE_MIN_SCALE]
	batchGenerateDrawables(argv[1],argv[2],ms=ms,ass=ass,iss=iss)

if __name__ == '__main__':
	domain(sys.argv)