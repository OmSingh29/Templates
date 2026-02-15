#from math import gcd,lcm,log
#from collections import deque
#from bisect import bisect #bisect:>num ka index(0-based)
#from heapq import heappush,heappop
#from sortedcontainers import SortedList,SortedSet,SortedDict
#from fractions import Fraction

#input_file=open('input.txt','r')
output_file=open('input.txt','w')
from os import startfile

from sys import stdin,stdout
#stdin=input_file
stdout=output_file
input=lambda:stdin.readline().rstrip()
print=lambda *args,sep=' ',end='\n':stdout.write(sep.join(map(str,args))+end)

def out(l):
    print('\n'.join(map(str,l)))

def yes():
    print('YES')

def no():
    print('NO')

def solve():
    ans=[i for i in range(9001,10001)]
    print(len(ans))
    out(ans)
 
for case in range(1):
    solve()

#input_file.close()
output_file.close()
        
startfile('input.txt')
