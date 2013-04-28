#!/usr/bin/env python2
import sys

def ringsurface(out_r):

	in_r = out_r - 1
	out_a = out_r * out_r
	int_a = in_r * inr 
	
	return out_a - in_a


def solve(r,t):

	remain = t
	cr = r
	res = 1
	remain -= cr * cr

	while True:
		cr += 2
		remain -= ringsurface(cr)
		if remain <= 0:
			break
		res += 1

	return res

cases = int(sys.stdin.readline())

print cases
for case in range(cases):
	line = sys.stdin.readline()[:-1].split(" ")
	print line
	r = int(line[0])
	t = int(line[1])
	print "Case #%d: %s" % (case+1,solve(r,t))
		