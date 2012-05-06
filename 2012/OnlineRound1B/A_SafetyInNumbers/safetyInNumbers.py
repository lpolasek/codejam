#!/usr/bin/env python2
import sys
import math



def solve(linea):
	result = []
	x = sum(linea)
	X = 2.0 * x
	M = min(linea)
	each = X / len(linea)

	return [ 100.0 * (each - i) / x for i in linea ]

	for i in xrange(len(linea)):
		a = [ x for x in linea ]
		a.pop(i)
		M = min(a)
		print i, M, a
		p1 = 100.0 * (each - linea[i]) / x 
		p2 = 100.0 * ((M + x - linea[i]) / 2 ) / x
		result.append(min(p1,p2))
	return result

n = int(sys.stdin.readline())

for i in range(1,n+1):
        linea = [ int(x) for x in sys.stdin.readline()[:-1].split()[1:] ]
        result = solve(linea)
	out = " ".join( [ "%f" % f for f in result ] )
	out = " ".join( [ str(f) for f in result ] )
        print "Case #%d: %s" % (i, out)
# 	print "Case #%d: %d %f" % (i, sum(linea), 1.0 * sum(linea) / len(linea))