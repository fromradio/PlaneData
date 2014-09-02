# coding=utf-8
# 由雪煜完成
# 具体要求见 'data_analysis.py'


def variance_calculation(input):
	var = {}
	sum_all = {}
	mean_all = {}

	for plane in input:
		temp_sum = 0.0
		num = 0
		for start_time in input[plane]:
			temp_sum = temp_sum + input[plane][start_time]['d'] - start_time
			num = num + 1
		mean_all[plane] = temp_sum/num

	for plane in input:
		temp_sum = 0.0
		num = 0
		for start_time in input[plane]:
			temp_sum = temp_sum + (input[plane][start_time]['d'] - start_time - mean_all[plane])**2
			num = num + 1
		var[plane] = temp_sum/num

	return var