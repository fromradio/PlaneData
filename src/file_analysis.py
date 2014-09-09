# coding=utf-8

# 添加所需要的库
import xlrd
import time


def file_analysis(filename):
	# filename为需要分析的文件
	# A 为一个字典(dictionary)，里面包含的元素为
	# x={航班号:{起飞时间:{经过的站点：时间,...},..},...}
	""" 
	'planelist' is the wanted list
	'planelist' contains the name of plane, the time of fight, the point the plane passes by and the current time of flying
	'planes' is the list of planes
	'points' is the list storing all possible points
	"""
	# initialization
	planelist = {}
	planes = []
	points = []
	# file reading
	data = xlrd.open_workbook(filename)
	table = data.sheets()[0]
	nrows = table.nrows
	# iteration
	for rownum in range(1,nrows):
		rowlist = table.row_values(rownum)
		if rowlist[6]=='NULL' or rowlist[8]=='NULL':
			continue
		plane = rowlist[0]
		point = rowlist[7]
		# compute the time
		timebegin = time.mktime(time.strptime(str(int(rowlist[6])),'%Y%m%d%H%M'))
		timeend = time.mktime(time.strptime(str(int(rowlist[8])),'%Y%m%d%H%M'))
		rlist = [rowlist[0],int(rowlist[6]),rowlist[7],timeend-timebegin]
		planelist = list_update(planelist,rlist)
		if plane not in planes:
			planes.append(plane)
		if point not in points:
			points.append(point)
	return [planelist,planes,points]

def list_update(A,list):
	if A.has_key(list[0]):
		# the list has already been created
		if A[list[0]].has_key(list[1]):
			A[list[0]][list[1]].update({list[2]:list[3]})
		else:
			A[list[0]].update({list[1]:{list[2]:list[3]}})
	else:
		# initialzation of the list
		A.update({list[0]:{list[1]:{list[2]:list[3]}}})
	return A

def dataTransform(planelist):
	""" 
	transform the 'planelist' into the form we want
	"""
	pass


def test():
	# 测试函数
	A = file_analysis('../Resource/ZSPD-ZBAA.xlsx')
	# print A
	return A

if __name__ == '__main__':
	test()