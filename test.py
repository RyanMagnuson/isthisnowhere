from getZips import *

#test function pointsToCoor, manually use google maps to confirm
def test1():
	p = genPoints(20)
	p2 = pointsToCoor(p, -122.566947, 37.965880)
	print(p[1])
	print(p2[1])
	print(p[78])
	print(p2[78])

test1()