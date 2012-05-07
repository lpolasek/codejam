#!/usr/bin/env python2
import sys
import math


def solve(classes, superClasses):

	for sc in superClasses:
		bfs = [ sc ]
		i = 0
		while(i < len(bfs)):
			c = bfs[i]
			if( set(classes[c]).intersection(set(bfs)) ):
				return "Yes"
			bfs = bfs + classes[c]
			i += 1
	return "No"

n = int(sys.stdin.readline())

for i in range(1,n+1):
	nClasses = int(sys.stdin.readline())
	classes = []
	for c in xrange(nClasses):
		classes.append([])
	superClasses = []
	for c in xrange(nClasses):
		line = [ int(x)-1 for x in sys.stdin.readline().split()[1:] ]
		if( not line ):
			superClasses.append(c)
		for super in line:
			classes[super].append(c)

        result = solve(classes, superClasses)
        print "Case #%d: %s" % (i, result)
