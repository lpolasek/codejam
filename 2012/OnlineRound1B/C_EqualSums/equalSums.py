#!/usr/bin/env python2
import sys
import math

global a
global b

def check():

	return ( sum(a) == sum(b) ) and ( set(a) != set(b) ) and (len(a) > 0) and (len(b) > 0) 

def solve(i, nums):

	if(i == len(nums)):
		return check()

	if solve(i+1, nums): return True

	a.append(nums[i])
	if solve(i+1, nums): return True
	a.pop()

	b.append(nums[i])
	if solve(i+1, nums): return True
	b.pop()

	return False

n = int(sys.stdin.readline())

for i in range(1,n+1):
	a = []
	b = []
        nums = [ int(x) for x in sys.stdin.readline()[:-1].split()[1:] ]
        result = solve(0, nums)
        print "Case #%d:" % (i)
	if result:
		print ' '.join( [ "%d" % x for x in a ]) 
		print ' '.join( [ "%d" % x for x in b ])
	else:
		print "Impossible"

