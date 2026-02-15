#from math import *
#from collections import *
from bisect import bisect
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

def manacher(t):
    ##Length of longest palindrome having centre at index i (in p it is 2*i+1) is p[i]-1
    s=['#']+list('#'.join(t))+['#']
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

#Pass 1-based indexing for l and r
def checkPal(l,r,p):
    l-=1
    r-=1
    lp,rp=2*l+1,2*r+1
    return p[(lp+rp)//2]>=r-l+2


def z_func(s):
    ##z_list[i]=Maximum length l of prefix[0,i-1] which is also a substring[i,n-1]
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
 
def kmp(s):
    #pre[i]=Maximum length l of prefix[0,i-1] which is also a suffix[1,i]
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

def longest_common_subsequence_length(s,t):
    n,m=len(s),len(t)
    last=[0]*(m+1)
    for i in range(n):
        cur=[0]*(m+1)
        for j in range(m):
            if s[i]==t[j]:
                cur[j+1]=last[j]+1
            else:
                cur[j+1]=max(cur[j],last[j+1])
        last=cur
    return cur[-1]

def longest_common_subsequence(s,t):
    n,m=len(s),len(t)
    dp=[[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i]==t[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
    i,j=n,m
    ans=[]
    while i and j:
        if s[i-1]==t[j-1]:
            ans.append(s[i-1])
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return ''.join(ans[::-1])

def longest_increasing_subsequence_length(l)
    lis=[]
    for j in l:
        #For strictly increasing lis, use bisect_left
        ind=bisect(lis,j)
        if ind==len(lis):
            lis.append(j)
        else:
            lis[ind]=j
    return len(lis)

def longest_increasing_subsequence(l):
    #dp[i] denotes the length of lis (strictly inc.) ending at index i
    n=len(l)
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if l[j]<l[i]:        
                dp[i]=max(dp[i],dp[j]+1)
    ma,ind=0,-1
    for i,j in enumerate(dp):
        if ma<j:
            ma=j
            ind=i
    lis=[l[ind]]
    cur=ma-1
    for i in range(ind-1,-1,-1):
        if dp[i]==cur and lis[-1]>l[i]:
            lis.append(l[i])
            cur-=1
    return lis[::-1]

def longest_common_substring_length(s,t):
    n,m=len(s),len(t)
    last=[0]*(m+1)
    ans=0
    for i in range(n):
        cur=[0]*(m+1)
        for j in range(m):
            if s[i]==t[j]:
                cur[j+1]=last[j]+1
            else:
                cur[j+1]=0
            ans=max(ans,cur[j+1])
        last=cur
    return ans

def longest_common_substring(s,t):
    n,m=len(s),len(t)
    last=[0]*(m+1)
    length=0
    ind=-1
    for i in range(n):
        cur=[0]*(m+1)
        for j in range(m):
            if s[i]==t[j]:
                cur[j+1]=last[j]+1
            else:
                cur[j+1]=0
            if length<cur[j+1]:
                length=cur[j+1]
                ind=i
        last=cur
    ans=[]
    while length:
        ans.append(s[ind])
        ind-=1
        length-=1
    return ''.join(ans[::-1])


def solve():
    a=list(map(int,input().split()))
    print(longest_increasing_subsequence(a))
    s=input()
    t=input()
    print(longest_common_subsequence(s,t))
    print(manacher(s))
    n=len(s)
    kmp(s)
    z_list=z_func(s)
    print(z_list)
        
for _ in range(1):
    solve()
