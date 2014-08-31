# coding=utf-8

# 添加所需要的库

def file_analysis(filename):
	# 由松涛完成
	# filename为需要分析的文件
	# A 为一个字典(dictionary)，里面包含的元素为
	# x={航班号:{{飞行日期:[{起飞时间:{经过的站点：时间,...},..},...]}
	A = {}
	return A


def test():
	# 测试函数
	A = file_analysis('../Resource/ZSPD-ZBAA.xlsx')
	print A

if __name__ == '__main__':
	test()