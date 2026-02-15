#from math import gcd,lcm,log
#from collections import deque
#from bisect import bisect #bisect:>num ka index(0-based)
#from heapq import heappush,heappop
#from sortedcontainers import SortedList,SortedSet,SortedDict
#from fractions import Fraction

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *args,sep=' ',end='\n':stdout.write(sep.join(map(str,args))+end)

def out(l):
    print(' '.join(map(str,l)))

def yes():
    print('YES')

def no():
    print('NO')

def check1(x):
    days=0
    for a,b in ab:
        days+=a*x//b+1
    return days>=c

def check2(x):
    days=0
    for a,b in ab:
        days+=a*x//b+1
    return days<=c

def solve():
    global n,c,ab
    n,c=map(int,input().split())
    ab=[tuple(map(int,input().split())) for i in range(n)]
    maxia,maxib=0,0
    for a,b in ab:
        maxia=max(maxia,a)
        maxib=max(maxib,b)
    if maxia==0:
        if n==c:
            print(-1)
        else:
            print(0)
        return
    low,high=1,c*maxib
    while high-low>1:
        mid=(low+high)//2
        if check1(mid):
             high=mid
        else:
            low=mid+1
    if check1(low):
        lo=low
    else:
        lo=high
    low,high=1,c*maxib
    while high-low>1:
        mid=(low+high)//2
        if check2(mid):
            low=mid
        else:
            high=mid-1
    if check2(high):
        hi=high
    elif check2(low):
        hi=low
    else:
        hi=0
    print(hi-lo+1)
        
for _ in range(1):
    solve()
