#!/usr/bin/env python2
import sys

def palindrome(n):
	rev = 0
	i = n

	while (n > 0):
		rev = rev * 10 + n % 10;
		n /= 10;

	return i == rev

fq = []

def dfs(num, max):
	if num:
		n = int(num)
		if palindrome(n*n):
			fq.append(int(n*n))
		else: 
			return

	for x in [ '1', '2']:
		while True:
			xx = x + num + x[::-1]
			ixx = int(xx)
			if (ixx * ixx) > max:
				break

			dfs(xx,max)
			x += '0'

def recursive_generation():
	global fq
	fq = [9]
	MAX = 10**100
	
	for digit in [ '', '0', '1', '2' ]:
		dfs(digit,MAX)
	fq.sort()

def iterative_generation():
	global fq
	fq = [ 1, 4, 9 ]
	res = [ '', '0', '1', '2' ]
	toadd = [ '1', '2' ]
	current = 0

	while current < len(res):
		cur = res[current]
		current += 1
		for ta in toadd:
			a = ta
			while (len(cur)+2*len(a)) <= 51:
				num = int(a + cur + a[::-1])
				if palindrome(num*num):
					res.append(a + cur + a[::-1])
					fq.append(num*num)
				a += '0'


	fq.sort()

def bruteforce_generation():
	global fq
	for i in xrange(10 ** 7 * 2):
		if palindrome(i) and palindrome(i ** 2):
			fq.append(i ** 2)

# recursive_generation()
iterative_generation()
# bruteforce_generation()
# print len(fq),fq
# fq = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L, 100000020000001L] 

def solve(A,B):
	res = 0
	for x in fq:
		if (x >= A) and (x <= B):
			res += 1

	return res

cases = int(sys.stdin.readline())


for case in range(cases):
	line = sys.stdin.readline()[:-1].split(" ")
	A = int(line[0])
	B = int(line[1])
	print "Case #%d: %d" % (case+1,solve(A,B))
	