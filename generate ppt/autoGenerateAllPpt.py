#coding=utf-8

import glob
import os
import sys
import generatePpt

img_path = '/Users/XK/Pictures/beauty/'

default_dir = 'new/'

file_name = "美女"

index = 13

def get_dirs():
	result = []
	g = glob.glob(img_path + '*')
	for x in g:
		if os.path.isdir(x):
			result.append(x)
	return result

def gen_ppt(dir):
	while True:
		images = get_images(dir)
		if images is not None:
			result = generatePpt.generatePptWithImages(images,file_name + str(index))
			if result == 1:
				remove_images(images)
			else:
				return -1;
		else:
			print "the number of files is less than 5."
			break

def remove_images(images):
	for x in images:
		print "delete file:"+x
		os.remove(x)

def get_images(dir):
	global index
	g = glob.glob(dir + os.sep + '*')
	if len(g) >= 10:
		index += 1
		result = []
		for x in xrange(0,10):
			result.append(g[x])
		return result
	elif len(g) >= 5:
		index += 1
		result = []
		for x in xrange(1,len(g)):
			result.append(g[x])
		return result
	else:
		return None

def main():
	for x in get_dirs():
		print "generate ppt with the pictures in " + x
		gen_ppt(x)

if __name__ == '__main__':
	main()