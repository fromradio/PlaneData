# coding=utf-8
# 由静远完成
# 具体要求见 'data_analysis.py'

def hjy(D,L=[]):
	for i in D:
		j=D[i]
		if type(i)==int:
			L.append(i)
		if isinstance(j,dict):
			hjy(j)
		elif i=='d':
#这里的d代表终点字符，如果按照本问题的数据来看，应该改成‘ZBAA’
			L.append(j)
	return L

#A是输入的字典
def mean_calculation(A):
	mean = 0
	List=[]
	List=hjy(A)
	n=0
	n=len(List)/2
	t=0
	while t<n:
		mean=mean+List[2*t+1]-List[2*t]
		t=t+1
	mean=mean/n
	return mean