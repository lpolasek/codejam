#!/usr/bin/env python2
import sys
import math


def solve(linea):

	result = 0
	for i in linea:
		result ^= i
	if result > 0:
		return "NO"


	result = 0
	for i in linea[1:]:
		result += i

	return "%d" % result

n = int(sys.stdin.readline())

for i in range(1,n+1):
        linea = sys.stdin.readline()
        linea = [ int(x) for x in sys.stdin.readline()[:-1].split() ]
	linea.sort()
        result = solve(linea)
        print "Case #%d: %s" % (i, result)
