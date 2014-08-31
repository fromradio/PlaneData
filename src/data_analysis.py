# coding=utf-8
## 由静远完成
# 具体要求见 'data_analysis.py' 添加所需要的库
from mean_calculation import *
from variance_calculation import *
# input 格式
# 例如
# A={'CES5186':{201305262206:{'DOGAR':201305262329,'ZBAA':201305262343}}}
# 首先是航班号，然后是对应所有的飞行时间和经过的站台


def main():
	# 算法要求，计算出A里面'plane'到达'd'（终点）的均值和方差
	A = {'plane':{0:{'1':10,'d':20},50:{'2':70,'d':80}}}
	mean = mean_calculation(A)
	variance = mean_calculation(A)
	print mean,variance
	pass
if __name__ == '__main__':
	main()