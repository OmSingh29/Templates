from math import isqrt
#from collections import deque
#from bisect import bisect #bisect:>num ka index(0-based)
#from heapq import heappush,heappop
#from sortedcontainers import SortedList,SortedSet,SortedDict
#from fractions import Fraction

input_file=open('input.txt','r')
output_file=open('output.txt','w')
from os import startfile

from sys import stdin,stdout
stdin=input_file
stdout=output_file
input=lambda:stdin.readline().rstrip()
print=lambda *args,sep=' ',end='\n':stdout.write(sep.join(map(str,args))+end)

def out(l):
    print('\n'.join(map(lambda x:str(x[0])+' '+str(x[1]),l)))

def yes():
    print('YES')

def no():
    print('NO')

def sieve(n):
    global isprime,lp
    isprime,lp=[True]*(n+1),[1]*(n+1)
    isprime[0],isprime[1]=False,False
    lp[0],lp[1]=0,0
    for i in range(2,n+1):
        if not isprime[i]:
            continue
        if lp[i]==1:
            lp[i]=i
        for j in range(i*i,n+1,i):
            if lp[j]==1:
                lp[j]=i
            isprime[j]=False

def prime_factorisation(n):
    '''
    Returns a list of tuples where l[i]=(prime,cnt) in O(log(n))
    '''
    num=n
    prime_facs=[]
    num=n
    while num>1:
        last=lp[num]
        cnt=0
        while lp[num]==last:
            num//=last
            cnt+=1
        prime_facs.append((last,cnt))
    return prime_facs

def divisors(n):
    '''
    Returns list of divisors (not sorted) of n in O(no. of divs)
    '''
    if n==1:
        return [1]
    prime_facs=prime_factorisation(n)
    divs=[1]
    for prime,cnt in prime_facs:
        tot=len(divs)
        for i in range(tot-1,-1,-1):
            div=divs[i]
            for j in range(cnt):
                div*=prime
                divs.append(div)
    return divs

def check(num):
    req=num*num
    diff=req-tot
    divs=divisors(diff)
    for div in divs:
        sdiv=diff//div
        if 2<=div<=n and 2<=sdiv+1<=n and div!=sdiv+1:
            return div,sdiv+1
    return -1,-1

def solve():
    global n,tot
    n=int(input())
    par=[1]*(n+1)
    tot=n*(n+1)//2-1
    sq=isqrt(tot)
    if sq*sq!=tot:
        a,b=-1,-1
        cnt=0
        while a==b==-1:
            sq+=1
            a,b=check(sq)
            cnt+=1
            if cnt>=10:
                break
        if a==b==-1:
            print(-1)
            zero.append(n)
            return
        else:
            par[a]=b
    ans=[]
    for i,j in enumerate(par):
        if i>=2:
            ans.append((j,i))
    out(ans)

sieve(400001)
zero=[]
for _ in range(int(input())):
    solve()

print(zero)

input_file.close()
output_file.close()
        
startfile('output.txt')
