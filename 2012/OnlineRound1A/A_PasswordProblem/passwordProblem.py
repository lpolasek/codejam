#!/usr/bin/env python2
import sys
import math


def solve(A,B,coef):

	result = B+2
	c = 1.0
	for bk in xrange(A):
		c = c * coef[bk]
# 		result = min( result, (B - A + 2 * bk + 1) + (B + 1) * (1.0 - c ))
#                                       (B - i) + (A - i - 1) + (B + 1) * (1 - x)
#                                       (B + A - 2i - 1 + (B + 1) * (1 - x)
		#  check why ? :?
		result = min( result, (B - bk) + (A - bk - 1) + (B + 1) * (1 - c) )


	return result

n = int(sys.stdin.readline())

for i in range(1,n+1):
        linea = sys.stdin.readline()[:-1].split()
	A = int(linea[0])
	B = int(linea[1])
	coef = [ float(x) for x in sys.stdin.readline()[:-1].split() ]
# 	print coef
        result = solve(A, B, coef)
        print "Case #%d: %.6f" % (i, result)