#!/usr/bin/env python2
import sys
import math

TYPES = 11

def matrix(rows , cols, value):
	result = []
	for i in xrange(rows):
		result.append([ value ] * cols)
	return result

def solve(b,t,i=0):
	result = 0
	N = len(b)
	M = len(t)

	cumB = matrix(N+1, TYPES, 0)
	cumT = matrix(M+1, TYPES, 0)
	dp = matrix(N+1, M+1, 0) 

	for typ in xrange(1,TYPES):
		for i in xrange(N):
			cumB[i+1][typ] = cumB[i][typ]
			if (b[i][1] == typ):
				cumB[i+1][typ] += b[i][0];

		for i in xrange(M):
			cumT[i+1][typ] = cumT[i][typ]
			if (t[i][1] == typ):
				cumT[i+1][typ] += t[i][0];


	for i in xrange(N):
		for j in xrange(M):
			for ni in xrange(1,N+1):
				for nj in xrange(1,M+1):
					typ = b[i][1]
					countB = cumB[ni][typ] - cumB[i][typ]
					countT = cumT[nj][typ] - cumT[j][typ]
					dp[ni][nj] = max(dp[ni][nj], dp[i][j] + min(countB, countT))

	print "Boxes:"
	print '\n'.join([ str(x) for x in cumB])
	print

	print "Toys"
	print '\n'.join([ str(x) for x in cumT])
	print
	print "DP"
	print '\n'.join([ str(x) for x in dp])
	print
	return dp[N][M]

n = int(sys.stdin.readline())

for i in range(1,n+1):
        nums = [ int(x) for x in sys.stdin.readline().split() ]
	N = nums[0]
	M = nums[1]
	nums = [ int(x) for x in sys.stdin.readline().split() ]
	boxes = zip(nums[::2], nums[1::2])
	nums = [ int(x) for x in sys.stdin.readline().split() ]
	toys = zip(nums[::2], nums[1::2])

	result = 0
        result = solve(boxes, toys)
        print "Case #%d: %d" % (i, result)

