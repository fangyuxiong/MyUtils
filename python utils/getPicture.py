#coding=utf-8
import re
import os
import time
import urllib
import urllib2

Image_Path = "/Users/XK/Pictures/beauty/"

Default_File = "new/"

Url = "http://www.meizitu.com/a/"

url_middle = "_"

url_suffix = ".html"

Sleep = 2

Target = r'<img.+src="(.+?jpg)"[\s|]/>'

regxs = [r'(http.*jpg)']

sub_reg = 'http://img\d.\.'

sub_replace = 'http://www.'

pages = [5338,5359,5351,5284,5270,5251,5246,5241]

special_dir = True

def search_reg(url,reg):
	p = reg.search(url)
	if p is not None:
		g = p.group(1)
		return g
	return None

def sub_url(old):
	return old#re.sub(sub_reg,sub_replace,old)

def get_file_path(page):
	if special_dir:
		return Image_Path + str(page) +os.sep
	else:
		return Image_Path + Default_File

#找图片
def get_urls(url,page):
	dir_path = get_file_path(page)
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
	name = get_file_name(url)
	if os.path.exists(dir_path + name):
		print dir_path + name + " is exists!"
		return

	p = url
	for x in regxs:
		reg = re.compile(x);
		p = search_reg(p,reg)
		if p is None:
			return

	if p is not None:
		u = sub_url(p)
		try:
			print dir_path + name
			urllib.urlretrieve(u,dir_path + name)
		except Exception, e:
			print str(e)
			print name + ' fail'

#获取图片格式 默认png
def get_file_type(s):
	index = s.rfind('.')
	if index > 0:
		return s[index:]
	return '.png'

def get_file_name(s):
	index = s.rfind('/')
	if index > 0:
		return s[index+1:]
	return re.sub(':','_',time.ctime()[10:19])+get_file_type(s)

#找某些target下的图片
def get_href(page):
	try:
		s = urllib2.urlopen(page)
		hrefs = re.compile(Target)
		s = s.read()
		links = hrefs.findall(s)
		return links
	except Exception,e:
		print str(e)
		return None

def generate_url_1(text):
	if text == 1:
		return Url + url_suffix
	else:
		return Url + url_middle + str(text) + url_suffix

def generate_url_0(text):
	return Url + str(text) + url_suffix

def generate_url(text,flag=0):
	return FLAGS.get(flag)(text)

FLAGS={0:generate_url_0,1:generate_url_1}

def main():
	for x in pages:
		u = generate_url(x)
		href = get_href(u)
		if href is None:
			continue
		print "href:"+str(href)
		time.sleep(Sleep)
		for j in href:
			get_urls(j,x)

if __name__ == '__main__':
	main()