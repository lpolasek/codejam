#!/usr/bin/env python2
import sys
import math


def find_paths(i,superclass,classes):
	if (superclass == i): return [ i ]
	result = []

	for super in classes[i-1]:
		x = find_paths(super,superclass,classes)
		if(x): 
			result.append( [ i ] + x)

	return result

def solve(classes):

	indexed_classes = zip(range(1,len(classes)+1), classes)
	superclasses = [ x[0] for x in filter(lambda y: len(y[1]) == 0, indexed_classes) ]
	if len(superclasses) > 1: print superclasses
	return ""

	for (i,subclasses) in indexed_classes:
		for superclass in superclasses:
			paths = find_paths(i,superclass,classes)
			if (len(paths) > 1): return "Yes"

	return "No"

n = int(sys.stdin.readline())

for i in range(1,n+1):
	classes = []
	nClasses = int(sys.stdin.readline())
	for c in xrange(nClasses):
		classes.append([ int(x) for x in sys.stdin.readline().split()[1:] ])
        result = solve(classes)
        print "Case #%d: %s" % (i, result)
