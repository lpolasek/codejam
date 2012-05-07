#!/usr/bin/env python2
import sys
import math

def solve(b,t,i=0):
	if(len(b) == 0) or (len(t) == 0): return 0

	B = list(b)
	T = list(t)
	result = 0

	if( B[0][1] == T[0][1] ):
		m = min(B[0][0], T[0][0])
		result += m
		B[0] = (B[0][0] - m, B[0][1])
		T[0] = (T[0][0] - m, T[0][1])

		if(B[0][0] < 1): B.pop(0)
		if(T[0][0] < 1): T.pop(0)

		result+=solve(B,T,i+1)

	B = list(b)
	T = list(t)
	T.pop(0)
	while T and (B[0][1] != T[0][1]):
		T.pop(0)
	result = max( result, solve(B,T,i+1) )
	T = list(t)

	B = list(b)
	B.pop(0)
	while B and (B[0][1] != T[0][1]):
		B.pop(0)
	result = max( result, solve(B,T,i+1) )
	B = list(b)

# 	result = max( result, solve(B,T,i+1) )

	return result

n = int(sys.stdin.readline())

for i in range(1,n+1):
        nums = [ int(x) for x in sys.stdin.readline().split() ]
	N = nums[0]
	M = nums[1]
	nums = [ int(x) for x in sys.stdin.readline().split() ]
	boxes = zip(nums[::2], nums[1::2])
	nums = [ int(x) for x in sys.stdin.readline().split() ]
	toys = zip(nums[::2], nums[1::2])

	boxes2 = [ x[1] for x in boxes ]
	toys2 = [ x for x in filter(lambda y: y[1] in boxes2 , toys) ]

	count = 0
	while(count < len(toys2) ):
		while ( len(toys2)-1 > count ) and (toys2[count][1] == toys2[count+1][1]):
			toys2[count+1] = (toys2[count][0]+toys2[count+1][0], toys2[count+1][1])
			toys2.pop(count)
		count +=1

# 	if ( i in [ 7, 10, 11, 12, 13, 14]): continue
#  	if ( i in [ 7 ]): 
# 		print boxes2, toys2
# 		print
# 		break

	result = 0
        result = solve(boxes, toys2)
        print "Case #%d: %d" % (i, result)
# 	print boxes, toys
# 	print

