#!/usr/bin/env python2
import sys
import math

def show(lista):
	res = "["
	for l in range(len(lista)):
		if(l > 0):
			res += ", "
		res += lista[l]
	res += "]"
	return res

def reaction(res, opos):
	for o in opos:
		if (o[0] in res) and (o[1] in res):
			return True
	return False
	
def solve(comb,opos,invoke):
	res = []
	
	for i in invoke:
		if reaction(res, opos):
			res = []
		if(len(res) > 0):
			p = res[-1]+i
			if (p) in comb:
				res = res[:-1] + [ comb[p] ]
				continue
		res.append(i)

	if reaction(res, opos):
		res = []
	return res

entrada = sys.stdin.read().split()
cases = int(entrada.pop(0))

for case in range(cases):
	comb = {}
	opos = []
	C = int(entrada.pop(0))
	for c in range(C):
		tri = entrada.pop(0)
		c1 = tri[:-1]
		c2 = tri[:-1][::-1]
		res = tri[-1]
		comb[c1] = res
		comb[c2] = res
	D = int(entrada.pop(0))
	for d in range(D):
		opos.append(entrada.pop(0))
	N = int(entrada.pop(0))
	invoke = entrada.pop(0)
		
	print "Case #%d: %s" % (case+1,show(solve(comb,opos,invoke)))

		