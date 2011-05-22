#!/usr/bin/env python2
import sys
import math


def solve(N, pD, pG):
	return "Possible"
	return "Broken"

entrada = sys.stdin.read().split()
cases = int(entrada.pop(0))

for case in range(cases):
	moves = []
	N = int(entrada.pop(0))
	pD = int(entrada.pop(0))
	pG = int(entrada.pop(0))
	print "Case #%d: %s" % (case+1,solve(N, pD, pG))
