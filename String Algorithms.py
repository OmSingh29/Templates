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

#Length of longest palindrome having centre at index i(in p it is 2*i+1) is p[i]-1
def manacher(t):
    s=['#']
    for i in t:
        s.append(i)
        s.append('#')
    n=len(s)
    p=[1]*n
    l,r=1,1
    for i in range(1,n):
        p[i]=max(0,min(r-i,p[l+r-i]))
        while 0<=i-p[i] and i+p[i]<n and s[i-p[i]]==s[i+p[i]]:
            p[i]+=1
        if i+p[i]>r:
            l,r=i-p[i],i+p[i]
    return p

#l and r is 0-based indexing
def checkPal(l,r):
    lp=2*l+1
    rp=2*r+1
    return p[(lp+rp)//2]>=r-l+2


#z_list[i]=Maximum length l of prefix[0,i-1] which is also a substring[i,n-1]
def z_func(s):
    n=len(s)
    z_list=[0]*n
    left=0
    right=0
    for i in range(1,n):
        if i<right:
            z_list[i]=min(z_list[i-left],right-i)
        while i+z_list[i]<n and s[z_list[i]]==s[i+z_list[i]]:
            z_list[i]+=1
        if i+z_list[i]>right:
            left=i
            right=i+z_list[i]
    return z_list

#pre[i]=Maximum length l of prefix[0,i-1] which is also a suffix[1,i] 
def kmp(s):
    n=len(s)
    pre=[0]*n
    for i,j in enumerate(pre):
        if i==0:
            continue
        ma=pre[i-1]
        while(ma>0 and s[i]!=s[ma]):
            ma=pre[ma-1]
        if s[i]==s[ma]:
            ma+=1
        pre[i]=ma
    return pre

def solve():
    s=input()
    n=len(s)
    '''pre=[0]*n
    kmp(s)'''
    z_list=z_func(s)
    print(z_list)
        
for _ in range(int(input())):
    solve()
