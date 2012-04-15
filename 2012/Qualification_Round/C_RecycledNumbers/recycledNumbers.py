#!/usr/bin/env python2
import sys
import math
import pdb

def getRecycled(N,B):
	result = set([])
	for i in range(1,len(N)):
		b = N[i:]
		f = N[:i]
		rn = b+f
		if(rn[0] != '0') and (int(N) < int(rn)) and (int(rn) <= int(B)):
			result.add(int(rn))
 	return result

def solve(A,B):
	global cache
	result = 0
	for i in range(int(A),int(B)+1):
		if i in cache:
			for j in cache[i]:
				if j <= int(B):
					result += 1
	return result

global cache
cache = {}

for d in range(7):
	lo = int('1'+'0'*d)
	hi = int('9'*(d+1))
	if d == 6:
		hi = 2000001
	for i in range(lo,hi):
		ir = getRecycled( "%d" % i,hi)
		if ir:
			cache[i] = ir

n = int(sys.stdin.readline())
for i in range(1,n+1):
        linea = sys.stdin.readline()[:-1].split(' ')
	A = linea[0]
	B = linea[1]
        result = solve(A,B)
        print "Case #%d: %d" % (i, result)
