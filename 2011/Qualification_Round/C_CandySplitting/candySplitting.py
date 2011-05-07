#!/usr/bin/env python2
import sys
import math

def solve(candies):
	candies.sort()
	x = 0
	suma = 0
	for i in candies:
		x ^=  i
		suma += i
	if( x != 0):
		return "NO"
	return "%d"  % (suma-candies[0])

entrada = sys.stdin.read().split()
cases = int(entrada.pop(0))

for case in range(cases):
	candies = []
	N = int(entrada.pop(0))
	for i in range(N):
		candies.append(int(entrada.pop(0)))
	print "Case #%d: %s" % (case+1,solve(candies))

		