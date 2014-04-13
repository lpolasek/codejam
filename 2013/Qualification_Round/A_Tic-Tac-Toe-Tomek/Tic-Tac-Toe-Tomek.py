#!/usr/bin/env python2
import sys

def test(board,player,count,x,y,dx,dy):

# 	print (board,player,count,x,y,dx,dy)

	for c in xrange(0,count):
		if (board[y][x] != player) and (board[y][x] != 'T'):
			return False
		x += dx
		y += dy
	return True

def solve(board):
	for p in [ 'X', 'O' ]:
		for x in xrange(0,4):
			if test(board,p,4,x,0,0,1): return p+" won"
		for y in xrange(0,4):
			if test(board,p,4,0,y,1,0): return p+" won"
		if test(board,p,4,0,0,1,1): return p+" won"
		if test(board,p,4,3,0,-1,1): return p+" won"

	for l in board:
		if '.' in l: return "Game has not completed"

	return "Draw"

cases = int(sys.stdin.readline())

for case in range(cases):
	board = []
	for l in xrange(4):
		board.append(sys.stdin.readline()[:-1])
	sys.stdin.readline()[:-1]
	print "Case #%d: %s" % (case+1,solve(board))
		