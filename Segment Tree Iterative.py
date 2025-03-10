#from math import *
#from collections import *
#from bisect import *
#from heapq import *

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

class SegmentTree:
    
    def __init__(self,l):
        self.n=len(l)
        self.seg=[0]*(2*self.n)
        for i in range(self.n,2*self.n):
            self.seg[i]=l[i-self.n]
        for i in range(self.n-1,0,-1):
            self.seg[i]=self.merge(self.seg[2*i],self.seg[2*i+1])
        '''
        if orientation of the subarrays (left and right) matter,use
        '''
        '''
        self.n=1<<len(l).bit_length() if len(l)&(len(l)-1) else len(l)
        self.seg=[0]*(2*self.n)
        for i in range(self.n,2*self.n):
            if i-self.n>=len(l):
                self.seg[i]=float('-inf')    #Change as needed
            else:
                self.seg[i]=l[i-self.n]
        for i in range(self.n-1,0,-1):
            self.seg[i]=self.merge(self.seg[2*i],self.seg[2*i+1])
        '''

    #Pass 1 based indexing
    def update(self,ind,val):
        ind=ind+self.n-1
        self.seg[ind]=val
        while ind>1:
            ind>>=1
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1 based indexing
    def query(self,left,right):                  
        left=left+self.n-1
        right=right+self.n-1
        
        if left==right:
            return self.seg[left]

        res=float('-inf')
            
        while left<=right:
            if left&1:
                res=self.merge(res,self.seg[left])
                left+=1
            if not right&1:
                res=self.merge(res,self.seg[right])
                right-=1
            left>>=1
            right>>=1
        return res

    def merge(self,a,b):
        return max(a,b)

class SegmentTreeWithIndex:
    
    def __init__(self,l):
        self.n=len(l)
        self.seg=[0]*(2*self.n)
        self.ind=[0]*(2*self.n)
        for i in range(self.n,2*self.n):
            self.seg[i]=l[i-self.n]
            self.ind[i]=i-self.n+1
        for i in range(self.n-1,0,-1):
            if self.seg[2*i]>=self.seg[2*i+1]:
                self.ind[i]=self.ind[2*i]
            else:
                self.ind[i]=self.ind[2*i+1]
            self.seg[i]=max(self.seg[2*i],self.seg[2*i+1])

    #Pass 1 based indexing
    def update(self,i,val):
        i=i+self.n-1
        self.seg[i]=val
        while i>1:
            i>>=1
            if self.seg[2*i]>=self.seg[2*i+1]:
                self.ind[i]=self.ind[2*i]
            else:
                self.ind[i]=self.ind[2*i+1]
            self.seg[i]=max(self.seg[2*i],self.seg[2*i+1])

    #Pass 1 based indexing
    def query(self,left,right):                  
        left=left+self.n-1
        right=right+self.n-1
        
        if left==right:
            return self.seg[left],self.ind[left]

        res=float('-inf')
            
        while left<=right:
            if left&1:
                res=max(res,self.seg[left]) 
                left+=1
                if left==right:
                    i=self.ind[left]
            if not right&1:
                res=max(res,self.seg[right])
                right-=1
                if left==right:
                    i=self.ind[left]
            left>>=1
            right>>=1
            if left==right:
                i=self.ind[left]
        return res,i
        #Returns 1-based indexing
            
def solve():
    n=int(input())
    l=list(map(int,input().split()))
    obj=SegmentTree(l)
    q=int(input())
    for i in range(q):
        ty,left,right=map(int,input().split())
        if ty==1:
            print(obj.query(left,right))
        else:
            obj.update(left,right)
        
for _ in range(int(input())):
    solve()
