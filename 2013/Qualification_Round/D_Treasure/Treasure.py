#!/usr/bin/env python2
import sys


def solve(case,K,N,kt,keys, chestsU, chestsK):

	print "Chest Number  |  Key Type To Open Chest  |  Key Types Inside"
	print "--------------+--------------------------+------------------"
	for c in xrange(N):
		print "%-14d|  %-26d|  " % ( c+1, chestsU[c] ),
		print chestsK[c]


	f = open('case%02d.dot' % case, 'w')
	f.write("digraph {\n")
	for k in kt:
		extra = ""
		if k in keys:
			extra = "[color = red]"
		f.write("\tkey%02d %s;\n" % (k,extra))
		for c in xrange(N):
			if chestsU[c] == k:
				f.write("\tkey%02d -> chest%02d;\n" % (k,c+1))
	for c in xrange(N):
		f.write("\tchest%02d;\n" % (c+1))
		for k in chestsK[c]:
			f.write("\tchest%02d -> key%02d;\n" % (c+1,k))
	f.write("}\n")
	f.close()

	return 0

cases = int(sys.stdin.readline())
for case in range(cases):
	kt = set
	line = sys.stdin.readline()[:-1].split(" ")
	K = int(line[0])
	N = int(line[1])
	chestsU = []
	chestsK = []
	keys = [ int(x) for x in sys.stdin.readline()[:-1].split(" ") ]
	kt = kt.union(set(keys))
	for chest in xrange(N):
		line = [ int(x) for x in sys.stdin.readline()[:-1].split(" ") ]
		chestsU.append(line[0])
		chestsK.append(line[2:])
		kt = kt.union(set(line[2:]))

	print "Case #%d: %d" % (case+1,solve(case,K,N,kt,keys, chestsU, chestsK))

		