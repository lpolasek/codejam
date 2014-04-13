#!/usr/bin/env python2
import sys


def maximal(pattern,value,count,x,y,dx,dy):
	for c in xrange(count):
		if pattern[y][x] > value: return False
		x += dx
		y += dy
	return True

def solve(M,N,pattern):
	for x in xrange(M):
		for y in xrange(N):
			if not (maximal(pattern,pattern[y][x],N,x,0,0,1) or
				maximal(pattern,pattern[y][x],M,0,y,1,0)):
				return "NO"

	return "YES"

cases = int(sys.stdin.readline())

for case in range(cases):
	line = sys.stdin.readline()[:-1].split(" ")
	N = int(line[0])
	M = int(line[1])
	pattern = []
	for s in range(N):
		row = [ int(x) for x in sys.stdin.readline()[:-1].split(" ")]
		pattern.append(row)
	print "Case #%d: %s" % (case+1,solve(M,N,pattern))

		