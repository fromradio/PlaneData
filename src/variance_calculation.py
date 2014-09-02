# coding=utf-8
# 由雪煜完成
# 具体要求见 'data_analysis.py'


def variance_calculation(input):
	var = 0
		num = 0
	sum = 0.0
	mean = 0

	for plane in input:
		for start_time in input[plane]:
			sum = sum + input[plane][start_time]['d'] - start_time
			num = num +1

	mean = sum/num
	sum = 0

	for plane in input:
		for start_time in input[plane]:
			sum = sum + (input[plane][start_time]['d'] - start_time - mean)**2

	var = sum/num
	return var