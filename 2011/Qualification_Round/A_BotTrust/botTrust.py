#!/usr/bin/env python2
import sys
import math

def solve(moves):
	pos = { 'O': 1, 'B': 1 }
	time = 0
	last = moves[0][0]
	accum = 0
	for m in moves:
		steps = abs(pos[ m[0] ] - m[1])
		if m[0] == last:
			time += steps+1
			accum += steps+1
		else: # m[0] == '1':
			time += max(0,steps-accum)+1
			accum = max(0,steps-accum)+1
		last = m[0]
		pos[ m[0] ] = m[1]
		
	return time


entrada = sys.stdin.read().split()
cases = int(entrada.pop(0))

for case in range(cases):
	moves = []
	N = int(entrada.pop(0))
	for i in range(N):
		rbt = entrada.pop(0)
		btn = int(entrada.pop(0))
		moves.append( (rbt, btn) )
	print "Case #%d: %d" % (case+1,solve(moves))

		