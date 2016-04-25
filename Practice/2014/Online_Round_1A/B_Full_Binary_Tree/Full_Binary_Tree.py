#!/usr/bin/env python3
import sys

def maxdes(tree, parent, node):
	if len(node.nei) < ( 2 + (1 if parent else 0 )):
		return 1

	best = []
	for n in node.nei:
		child = tree[n]
		if child == parent:
			continue
		best.append(maxdes(tree,node,child))

	best.sort(reverse=True)
	return 1 + best[0] + best[1]

def solve(tree):
	res = 0
	for root in tree:
		res = max(res,maxdes(tree,None,root))
	return res

cases = int(sys.stdin.readline())

class Node:
	def __init__(self, id):
		self.id = id
		self.nei = []

	def __str__(self):
		return "%d: %s" % ( self.id, " ".join([ "%d" % x for x in self.nei ]))
		
for case in range(cases):
	N = int(sys.stdin.readline()[:-1])
	tree = []
	for n in range(N):
		tree.append(Node(n))

	for n in range(N-1):
		edge = [ int(x) - 1 for x in sys.stdin.readline()[:-1].split(' ') ]
		tree[edge[0]].nei.append(edge[1])
		tree[edge[1]].nei.append(edge[0])

	print("Case #%d: %d" % (case+1,N - solve(tree)))
