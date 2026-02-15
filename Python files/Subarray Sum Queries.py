#from math import gcd,lcm,log
#from collections import deque,defaultdict
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
 
class Node:
 
    def __init__(self,subarr_sum,prefix,suffix,total_sum):
        self.sub=subarr_sum
        self.pre=prefix
        self.suf=suffix
        self.tot=total_sum
 
    def __repr__(self):
        return f'Node({self.sub}, {self.pre}, {self.suf}, {self.tot})'
 
class SegmentTree:
    
    def __init__(self,l,merge,default):
        self.merge=merge
        self.default=default
        self.n=1<<len(l).bit_length() if len(l)&(len(l)-1) else len(l)
        self.seg=[self.default for i in range(2*self.n)]
        for i in range(self.n,2*self.n):
            if i-self.n>=len(l):
                break
            else:
                self.seg[i]=l[i-self.n]
        for i in range(self.n-1,0,-1):
            self.seg[i]=self.merge(self.seg[2*i],self.seg[2*i+1])
 
    #Pass 1 based indexing
    def update(self,ind,val):
        ind=ind+self.n-1
        self.seg[ind]=val
        while ind>1:
            ind>>=1
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])
 
    #Pass 1 based indexing
    def query(self,left,right):                  
        left,right=left+self.n-1,right+self.n-1
 
        resL,resR=self.default,self.default    #Default value
            
        while left<=right:
            if left&1:
                resL=self.merge(resL,self.seg[left])
                left+=1
            if not right&1:
                resR=self.merge(self.seg[right],resR)
                right-=1
            left>>=1
            right>>=1
        return self.merge(resL,resR)
 
    #Pass 1 based indexing
    def get_element(self,ind):
        return self.seg[self.n+ind-1]
 
def merge(nodeL,nodeR):
    subarr_sum=max(nodeL.sub,nodeR.sub,nodeL.suf+nodeR.pre)
    prefix=max(nodeL.pre,nodeL.tot+nodeR.pre if nodeR.pre!=float('-inf') else nodeL.tot)
    suffix=max(nodeL.suf+nodeR.tot if nodeL.suf!=float('-inf') else nodeR.tot,nodeR.suf)
    total_sum=nodeL.tot+nodeR.tot if nodeL.tot!=float('-inf') and nodeR.tot!=float('-inf') else max(nodeL.tot,nodeR.tot)
    return Node(subarr_sum,prefix,suffix,total_sum)
 
 
def solve():
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    default=Node(float('-inf'),float('-inf'),float('-inf'),float('-inf'))
    seg=SegmentTree([Node(j,j,j,j) for j in a],merge,default)
    ans=[]
    for i in range(q):
        i,x=map(int,input().split())
        seg.update(i,Node(x,x,x,x))
        ans.append(max(0,seg.query(1,n).sub))
    out(ans)
        
for _ in range(1):
    solve()
