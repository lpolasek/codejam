#!/usr/bin/env python2
import sys
import math
import pdb

def getMaxScore(score, surprising):
	average = score // 3
	reminder = score % 3

	if reminder:
		if surprising:
			if (reminder == 2) and ((average + 2) <= 10):
				return average + 2
			if (reminder == 1) and ((average + 1) <= 10) and (score > 1):
				return average + 1
		else:
			return average + 1
	else:
		if surprising and score and ((average + 1) <= 10):
			return average + 1
		elif not surprising:
			return average

	return -10000

def solve(S,p,scores,i=0):
	global cache

	if (i == len(scores)):
		if (S != 0):
			return -10000
		else:
			return 0

	if cache[i][S] != -1:
		return cache[i][S]

	maxi = -10000
	score = scores[i]

	ms = getMaxScore(score, False)
	if( ms >= 0 ):
		sol = (solve(S,p,scores,i+1))
		maxi = max(maxi, int(ms >= p) + sol)

	ms = getMaxScore(score, True)
	if( ms >= 0 ) and S:
		sol = (solve(S-1,p,scores,i+1))
		maxi = max(maxi, int(ms >= p) + sol)

	cache[i][S] = maxi
	return cache[i][S]

n = int(sys.stdin.readline())

for i in range(1,n+1):
        linea = [ int(x) for x in sys.stdin.readline()[:-1].split(' ')]
	N = linea[0]
	S = linea[1]
	p = linea[2]
	scores = linea[3:]
	global cache
	cache = []
	for x in range(101):
		cache.append( [-1] * 101)
	assert len(scores) == N
        result = max(0,solve(S,p,scores))
        print "Case #%d: %d" % (i, result)
