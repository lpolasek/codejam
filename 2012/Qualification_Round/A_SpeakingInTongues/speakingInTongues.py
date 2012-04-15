#!/usr/bin/env python2
import sys
from string import maketrans
import math


intab  = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq"
outtab = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz"
trantab = maketrans(intab, outtab)

def solve(linea):

	return linea.translate(trantab)

# entrada = sys.stdin.read().split()
n = int(sys.stdin.readline())

for i in range(1,n+1):
        linea = sys.stdin.readline()[:-1]
        result = solve(linea)
        print "Case #%d: %s" % (i, result)