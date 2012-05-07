#!/usr/bin/env python2
import sys
import math


linea = [ int(x) for x in sys.stdin.readline().split() ]
N = linea[0]
A = linea[1]
B = linea[2]
values = []
sums = set([])

for i in xrange(N):
	values.append(int(sys.stdin.readline()))

