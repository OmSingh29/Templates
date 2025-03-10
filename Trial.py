#from math import ceil,log,lcm,gcd,isfinite
#from collections import deque,Counter
#from bisect import bisect #bisect:>num ka index(0-based)
#from heapq import heappush,heappop
#from sortedcontainers import SortedList,SortedSet,SortedDict
#from random import randint

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *args,sep=' ',end='\n':stdout.write(sep.join(map(str,args))+end)

def out(l):
    print('\n'.join(map(str,l)))

def yes():
    print('YES')

def no():
    print('NO')

def alice():
    print('ALICE')

def bob():
    print('BOB')

def solve():
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    ans=s
    for i in range(1,1<<n):
        cur=0
        num=1
        for j in range(n):
            if num&i:
                cur+=l[j]
            num<<=1
        ans=min(ans,abs(s-cur-cur))
    print(ans)
        
for _ in range(1):
    solve()
