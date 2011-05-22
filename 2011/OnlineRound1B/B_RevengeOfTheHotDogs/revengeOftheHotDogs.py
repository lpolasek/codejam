#!/usr/bin/env python2
import sys
import math

WPs = []
OWPs = []
OOWPs = []


def WP(team):
	return float(team.count('1')) / ( team.count('0') + team.count('1') )

def OWP(i, board):
	res = 0.0
	count = 0
	for r in range(len(board)):
		if(board[r][i] == '.'): continue
		team = board[r][:i]+board[r][i+1:]
		count += 1
		res += WP(team)
		
	return res / count

def OOWP(i, board):
	res = 0.0
	count = 0
	for r in range(len(board)):
		if(board[r][i] == '.'): continue
		count += 1
		res += OWPs[r]
		
	return res / count

def solve(board):
	res = []
	for i in range(len(board)):
		WPs.append( WP(board[i]) )
		OWPs.append( OWP(i, board) )
	for i in range(len(board)):
		OOWPs.append( OOWP(i, board) )
		RPI = 0.25 * WPs[i] + 0.50 * OWPs[i] + 0.25 * OOWPs[i]
# 		res.append(RPI)
		res.append(RPI)
	return res

entrada = sys.stdin.read().split()
cases = int(entrada.pop(0))

for case in range(cases):
	WPs = []
	OWPs = []
	OOWPs = []
	board = []
	teams = int(entrada.pop(0))
	for t in range(teams):
		board.append(entrada.pop(0))
# 	print board
	res = solve(board)
	print "Case #%d:" % (case+1)
	for r in res:
		print "%0.12f" % r

