#!/usr/bin/env python2
import sys
import math


def solve(w, n):

	res = 0
	vowels = "aeiou"
	last = 0
	conse = 0
	for i in xrange(len(w)):
		if w[i] in vowels:
			conse = 0
		else:
			conse += 1

		if conse >= n:
			last = i - (n-1) + 1

		if last >= 0:
			res += last
	return res

n = int(sys.stdin.readline())
for i in range(1,n+1):
        linea = sys.stdin.readline()[:-1].split()
	w = linea[0]
	n = int(linea[1])
        print "Case #%d: %s" % (i, solve(w,n))
