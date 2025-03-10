#from math import *
#from collections import *
#from bisect import *
#from heapq import *
#from random import *

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)

def out(l):
    print(' '.join(map(str,l)))

def yes():
    print('Yes')

def no():
    print('No')

def alice():
    print('Alice')

def bob():
    print('Bob')

mod=1000000007

def add(x,y):
    c=((x%mod)+(y%mod))%mod
    return c

def mul(x,y):
    c=((x%mod)*(y%mod))%mod
    return c

def get_inv(y):
    # Always use import math for this function
    a=pow(y,mod-2,mod)
    return a

def getHash(s):
    value=0
    p=1
    prime=31
    for i,j in enumerate(s):
        value=add(value,mul(ord(j)-ord('a')+1,p))
        dp[i+1]=value
        p=mul(prime,p)
        inv[i+1]=get_inv(p)

def solve():
    global inv,dp,s,pre
    s=input()
    n=len(s)
    inv=[0]*(n+1)
    inv[0]=1
    dp=[0]*(n+1)
    getHash(s)
    '''q=int(input())
    for i in range(q):
        si=input()
        print(subHash(si))'''
        
for _ in range(int(input())):
    solve()
