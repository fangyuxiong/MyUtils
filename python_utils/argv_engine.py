# coding=utf-8

# 处理sys.argv的工具

def process_argv(argv,keys,offset=-1):
	l = len(argv)
	if l <= offset:
		return None
	arr = {}
	for key in keys:
		try:
			i = argv.index(key)
			if i >= 0 and (i + 1) < l and i > offset:
				v = argv[i + 1]
				if not v in keys:
					arr[key] = v
		except Exception, e:
			continue
	return arr