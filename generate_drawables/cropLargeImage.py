#coding=utf-8

from PIL import Image
import os
import sys
import glob

def cropAndSave(res,rect,name):
	print 'rect : '+str(rect) + ' name is:'+name
	crop = res.crop(rect)
	crop.save(name)

def name(res,x,y):
	name = os.path.split(res)[1]
	suffix = os.path.splitext(res)[1]
	l = len(suffix)
	if l > 0:
		l = -l
	else:
		l = len(name)
	name = name[0:l]
	return name + str(x) + '_' +str(y) + suffix

def batchCrop(res,width,height,path):
	image = Image.open(res)
	maxSize = image.size
	maxWidth = maxSize[0]
	maxHeight = maxSize[1]
	print 'width : %d , height : %d'%(maxWidth,maxHeight)
	wt = maxWidth / width
	ht = maxHeight / height
	print 'wt : %d , ht : %d '%(wt,ht)
	for x in xrange(0,wt):
		for y in xrange(0,ht):
			top = y * height
			left = x * width
			rect = (left,top,left+width,top+height)
			cropAndSave(image,rect,path + os.sep + name(res,x,y))

def main(argvs):
	l = len(argvs)
	res = ""
	width = ""
	height = ""
	path = ""
	if l == 3:
		res = argvs[1]
		width = int(argvs[2])
		height = width
	elif l == 4:
		res = argvs[1]
		width = int(argvs[2])
		height = int(argvs[3])
	elif l == 5:
		res = argvs[1]
		width = int(argvs[2])
		height = int(argvs[3])
		path = argvs[4]
	if res == "" or width == "" or height == "":
		print "error"
		return
	if path == "":
		path = os.path.split(res)[0]
	# print "res : %s , width : %d , height : %d , path : %s"%(res,width,height,path)

	batchCrop(res,width,height,path)

if __name__ == '__main__':
	main(sys.argv)
