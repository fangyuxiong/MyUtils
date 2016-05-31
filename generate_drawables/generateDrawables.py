#coding=utf-8
from PIL import Image
import os
import sys

IMAGE_PATH_EXTRA = "-p"

IMAGE_OUTPATH_EXTRA = "-op"

IMAGE_OUTNAME_EXTRA = "-on"

IMAGE_MAX_SCALE = "-as"

IMAGE_MIN_SCALE = "-is"

IMAGE_MAX_SIZE = "-ms"

DRAWABLE = "drawable"

MIPMAP = "mipmap"

def resize_img(img_path,out_path,out_name,img_size):
	try:
		img_size = (int(img_size[0]),int(img_size[1]))
		img = Image.open(img_path)
		out = img.resize(img_size,Image.ANTIALIAS)
		if not os.path.exists(out_path):
			os.makedirs(out_path)
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
		return "NameValue[name : %s , value : %f]"%(self.name,self.value)

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
		max_size = 0
		if abs(p - op) == 1:
			error_argv()
			return None
		if l == p or l == op:
			error_argv()
			return None
		try:
			on = argv.index(IMAGE_OUTNAME_EXTRA)
			if not check_index(p,op,on):
				return None
		except Exception, e:
			on = -1
		try:
			maxs = argv.index(IMAGE_MAX_SCALE)
			if not check_index(p,op,maxs):
				return None
		except Exception, e:
			maxs = -1
		try:
			mins = argv.index(IMAGE_MIN_SCALE)
			if not check_index(p,op,mins):
				return None
		except Exception, e:
			mins = -1
		try:
			max_size = argv.index(IMAGE_MAX_SIZE)
			if not check_index(p,op,max_size):
				return None
		except Exception, e:
			max_size = -1

		if not os.path.isfile(argv[p+1]):
			print 'path: "%s" is not a file or not exists.'%argv[p+1]
			return None
		outPath = argv[op+1]
		outName = os.path.split(outPath)[1]

		if outName != DRAWABLE and outName != MIPMAP:
			outPath = outPath + os.sep + DRAWABLE

		array = {IMAGE_PATH_EXTRA:argv[p+1] , IMAGE_OUTPATH_EXTRA:outPath}

		if check_index_other(on,[p,op,maxs,mins,max_size]):
			array[IMAGE_OUTNAME_EXTRA] = argv[on + 1]
		else:
			array[IMAGE_OUTNAME_EXTRA] = os.path.split(argv[p+1])[1]
		if check_index_other(maxs,[p,op,on,mins,max_size]):
			array[IMAGE_MAX_SCALE] = argv[maxs + 1]
		else:
			array[IMAGE_MAX_SCALE] = 'xxx'
		if check_index_other(mins,[p,op,on,maxs,max_size]):
			array[IMAGE_MIN_SCALE] = argv[mins + 1]
		else:
			array[IMAGE_MIN_SCALE] = 'l'
		if check_index_other(max_size,[p,op,on,maxs,mins]):
			array[IMAGE_MAX_SIZE] = argv[max_size + 1]
		else:
			array[IMAGE_MAX_SIZE] = Image.open(argv[p+1]).size
		return array

def check_index_other(i,others):
	if i > 0:
		for x in others:
			if i + 1 == x:
				return False
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

def change_size_to_tuple(size):
	if isinstance(size,tuple):
		return size
	elif size.find('-') > -1:
		ss = size.split('-')
		return (int(ss[0]),int(ss[1]))
	return None

def get_size(old_size,old_scale,new_scale):
	os = old_scale.value
	ns = new_scale.value
	ow = old_size[0]
	oh = old_size[1]
	if ns > os:
		return (ow,oh)
	nw = ow / os * ns
	nh = oh / os * ns
	return (nw,nh)

def change_size(arr):
	if arr is None:
		return None
	if IMAGE_MAX_SCALE in arr:
		size = arr[IMAGE_MAX_SCALE]
		if not size in ScaleType.enum:
			error_scale()
			return None
		else:
			arr[IMAGE_MAX_SCALE] = change_scale_to_scale_type(size)
	if IMAGE_MIN_SCALE in arr:
		size = arr[IMAGE_MIN_SCALE]
		if not size in ScaleType.enum:
			error_scale()
			return None
		else:
			arr[IMAGE_MIN_SCALE] = change_scale_to_scale_type(size)
	if IMAGE_MAX_SIZE in arr:
		size = arr[IMAGE_MAX_SIZE]
		size = change_size_to_tuple(size)
		if not size:
			error_size()
			return None
		else:
			arr[IMAGE_MAX_SIZE]	= size
	return arr

def error_argv():
	print '''useage: generateDrawable.py -p image_path -op out_path [-extra argv]
-p  : the image path
-op : the image out path
extra:
	-on : the image out name,if not set, use the old image name.
	-ms : the max size of output image,if not set, use the old image size.
		eg:	100-100
	-as : the max scale of image
		xxx | xx | x | h | m | l
		if not set, the max scale is "xxx".
	-is : the min scale of image 
		xxx | xx | x | h | m | l
		if not set, the min scale is "l".'''

def error_scale():
	print '''the min or max scale of image must one value of these:
	xxx | xx | x | h | m | l'''

def error_size():
	print '''the max size of output image should set like this:	100-100'''

def main(argv):
	arr = change_size(process_argv(argv))
	if arr is None:
		return -1

	max_scale = arr[IMAGE_MAX_SCALE]
	min_scale = arr[IMAGE_MIN_SCALE]
	for x in ScaleType.enum:
		st = change_scale_to_scale_type(x)
		if st.value >= min_scale.value:
			ns = get_size(arr[IMAGE_MAX_SIZE],max_scale,st)
			res = arr[IMAGE_PATH_EXTRA]
			out_path = arr[IMAGE_OUTPATH_EXTRA]+"-"+st.name
			out_name = arr[IMAGE_OUTNAME_EXTRA]
			resize_img(res,out_path,out_name,ns)

if __name__ == '__main__':
	main(sys.argv)

