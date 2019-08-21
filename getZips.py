#getZips.py
#Gets the zip codes in a given radius

from math import pi


def genPoints(radius, lat, lon):

	#first getting sample points in km distance from original
	pointsKM = []
	pointsKM.append((0, 0))

	#radius of concentric circles
	for x in range(1, radius + 1):

		#num of slices needed
		num = 2 * (2 ** x)

		#angle size of those slices
		a = (2 * pi) / num

		for i in range(num):
			pointsKM.append(( , ))		#storing in (x, y) format




