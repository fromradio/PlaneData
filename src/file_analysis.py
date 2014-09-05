# coding=utf-8

# 添加所需要的库
import xlrd

def file_analysis(filename):
	# 由松陶完成
	# filename为需要分析的文件
	# A 为一个字典(dictionary)，里面包含的元素为
	# x={航班号:{起飞时间:{经过的站点：时间,...},..},...}
	A = {}
	data = xlrd.open_workbook(filename)
	table = data.sheets()[0]
	nrows = table.nrows
	for rownum in range(1,nrows):
		rowlist = table.row_values(rownum)
		if rowlist[6]=='NULL' or rowlist[8]=='NULL':
			continue
		rlist = [rowlist[0],int(rowlist[6]),rowlist[7],int(rowlist[8])]
		A = myupdate(A,rlist)
	return A

def myupdate(A,list):
	if A.has_key(list[0]):
		if A[list[0]].has_key(list[1]):
			A[list[0]][list[1]].update({list[2]:list[3]})
		else:
			A[list[0]].update({list[1]:{list[2]:list[3]}})
	else:
		A.update({list[0]:{list[1]:{list[2]:list[3]}}})
	return A



def test():
	# 测试函数
	A = file_analysis('C:/Users/GoStone/learngit/PlaneData/Resource/ZSPD-ZBAA.xlsx')
	print A

if __name__ == '__main__':
	test()