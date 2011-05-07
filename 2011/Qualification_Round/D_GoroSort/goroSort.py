#!/usr/bin/env python2
import sys
import math

def solve(numbers):
	missed = 0
	for i in range(len(numbers)):
		if (i+1) != numbers[i]: missed +=1
	#swaps = math.ceil(missed/2)
	return missed
	
	
entrada = sys.stdin.read().split()
cases = int(entrada.pop(0))

for case in range(cases):
	numbers = []
	N = int(entrada.pop(0))
	for i in range(N):
		numbers.append(int(entrada.pop(0)))
	print "Case #%d: %.6f" % (case+1,solve(numbers))

		