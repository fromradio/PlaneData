# coding = utf-8
# transform the data into the form we can analyze


def pointTimeList(planelist,plane,point):
	"""
	input:
		planelist: the list that storing the information
		plane: the plane that we are finding
		point: the point we are finding
	output:
		the time list of current plane and point
	"""
	if plane in planelist:
		# we find the plane in the planelist
		pointtimelist=[]
		for timebegin in planelist[plane].keys():
			# traverse all possible time
			if point in planelist[plane][timebegin]:
				pointtimelist.append(planelist[plane][timebegin][point])
		if pointtimelist == []:
			print "Warning: the list is empty meaning that the plane has not passed the point yet"
		return pointtimelist
	else:
		print "Warning: we do not find the corresponding flight in the list"
		return []