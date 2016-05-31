#coding=utf-8
from PIL import Image
import os
import sys

IMAGE_PATH_EXTRA = "-p"

IMAGE_OUTPATH_EXTRA = "-op"

IMAGE_OUTNAME_EXTRA = "-on"

IMAGE_MAX_SIZE = "-as"

IMAGE_MIN_SIZE = "-is"

def resize_img(img_path,out_path,out_name,img_size):
	try:
		img = Image.open(img_path)
		out = img.resize(img_size,Image.ANTIALIAS)
		out.save(out_path + os.sep + out_name , quality = 100)
	except Exception, e:
		print e

class NameValue:
	name = ""
	value = 0
	def __init__(self, name, value):
		self.name = name
		self.value = value
	def __str__(self):
		return "NameValue[name : %s , value : %d]"%(self.name,self.value)

class ScaleType:
	XXXHDPI = NameValue("xxxhdpi" , 4)
	XXHDPI  = NameValue("xxhdpi"  , 3)
	XHDPI   = NameValue("xhdpi"   , 2)
	HDPI    = NameValue("hdpi"    , 1.5)
	MDPI    = NameValue("mdpi"    , 1)
	LDPI    = NameValue("ldpi"    , 0.75)
	enum	= ["xxx" , "xx" , "x" , "h" , "m" , "l"]
	def __str__(self):
		return "ScaleType"

def process_argv(argv):
	l = len(argv)
	if not ((IMAGE_PATH_EXTRA in argv) and (IMAGE_OUTPATH_EXTRA in argv)):
		error_argv()
		return None
	else:
		p = argv.index(IMAGE_PATH_EXTRA)
		op = argv.index(IMAGE_OUTPATH_EXTRA)
		on = 0
		maxs = 0
		mins = 0
		if abs(p - op) == 1:
			error_argv()
			return None
		if l == p or l == op:
			return None
		try:
			on = argv.index(IMAGE_OUTNAME_EXTRA)
			if not check_index(p,op,on):
				return None
		except Exception, e:
			on = -1
		try:
			maxs = argv.index(IMAGE_MAX_SIZE)
			if not check_index(p,op,maxs):
				return None
		except Exception, e:
			maxs = -1
		try:
			mins = argv.index(IMAGE_MIN_SIZE)
			if not check_index(p,op,mins):
				return None
		except Exception, e:
			mins = -1
		array = {IMAGE_PATH_EXTRA:argv[p+1] , IMAGE_OUTPATH_EXTRA:argv[op+1]}
		if check_index_other(on,p,op,maxs,mins):
			array[IMAGE_OUTNAME_EXTRA] = argv[on + 1]
		if check_index_other(maxs,p,op,on,mins):
			array[IMAGE_MAX_SIZE] = argv[maxs + 1]
		if check_index_other(mins,p,op,on,maxs):
			array[IMAGE_MIN_SIZE] = argv[mins + 1]
		return array

def check_index_other(i,a1,a2,a3,a4):
	if i > 0 and (i+1!=a1 or i+1!=a2 or i+1!=a3 or i+1!=a4):
		return True
	return False

def check_index(p,op,other):
	if abs(p - other) == 1:
		error_argv()
		return False
	if abs(op - other) == 1:
		error_argv()
		return False
	return True

def change_scale_to_scale_type(s):
	enum = ScaleType.enum
	if s == enum[0]:
		return ScaleType.XXXHDPI
	if s == enum[1]:
		return ScaleType.XXHDPI
	if s == enum[2]:
		return ScaleType.XHDPI
	if s == enum[3]:
		return ScaleType.HDPI
	if s == enum[4]:
		return ScaleType.MDPI
	if s == enum[5]:
		return ScaleType.LDPI
	return None

def error_argv():
	print '''useage: generateDrawable.py -p image_path -op out_path [-extra argv]
-p  : the image path
-op : the image out path
extra:
	-on : the image out name
	-as : the max size of image 
		xxx | xx | x | h | m | l
	-is : the min size of image 
		xxx | xx | x | h | m | l'''

def error_size():
	print '''the min or max size of image must one value of these:
	xxx | xx | x | h | m | l'''

def main():
	arr = process_argv(sys.argv)
	if arr is None:
		return -1
	if IMAGE_MAX_SIZE in arr:
		size = arr[IMAGE_MAX_SIZE]
		if not size in ScaleType.enum:
			error_size()
			return -1
		else:
			arr[IMAGE_MAX_SIZE] = change_scale_to_scale_type(size)
	if IMAGE_MIN_SIZE in arr:
		size = arr[IMAGE_MIN_SIZE]
		if not size in ScaleType.enum:
			error_size()
			return -1
		else:
			arr[IMAGE_MIN_SIZE] = change_scale_to_scale_type(size)
	print str(arr)

if __name__ == '__main__':
	main()

