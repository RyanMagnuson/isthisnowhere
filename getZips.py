#getZips.py
#Gets the zip codes in a given radius

# test lon: -122.566947
# test lat: 37.965880

import math


def genPoints(radius):

	#first getting sample points in km distance from original
	points = []
	points.append((0, 0))

	#radius of concentric circles
	for r in range(1, radius + 1):

		#num of slices needed
		num = 2 * (2 ** r)

		#angle size of those slices
		a = (2 * math.pi) / num

		for i in range(num):	#storing in (x, y) format
			points.append(( r * (math.cos(i * a)), r * (math.sin(i * a))))

	return points


def pointsToCoor(points, lon, lat):

	#long 'like' x, lat like y
	return list(map(lambda coor: (lon + (180/math.pi)*(coor[0]/6371)/math.cos(lon*math.pi/180), lat + (180/math.pi)*(coor[1]/6371)), points))


