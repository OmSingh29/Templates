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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

#Both are tried and tested

class SegmentTree:

    def __init__(self,l,merge,default):
        self.merge=merge
        self.default=default
        self.l=l
        self.n=len(l)
        self.seg=[self.default for i in range(4*self.n)]
        self.build(0,0,self.n-1)

    def build(self,ind,low,high):
        if low==high:
            self.seg[ind]=self.l[low]
            return
        mid=(low+high)//2
        self.build(2*ind+1,low,mid)
        self.build(2*ind+2,mid+1,high)
        self.seg[ind]=self.merge(self.seg[2*ind+1],self.seg[2*ind+2])

    def update(self,i,val):
        return self.upd(0,0,self.n-1,i-1,val)

    #Pass 0-based indexing as (0,0,n-1,ind,val to be assigned)
    def upd(self,ind,low,high,i,val):
        if low==high==i:
            self.seg[ind]=val
            return
        mid=(low+high)//2
        if low<=i<=high:
            if i<=mid:
                self.upd(2*ind+1,low,mid,i,val)
            else:
                self.upd(2*ind+2,mid+1,high,i,val)
            self.seg[ind]=self.merge(self.seg[2*ind+1],self.seg[2*ind+2])

    def query(self,left,right):
        return self.que(0,0,self.n-1,left-1,right-1)

    #Pass 0-based indexing as (0,0,n-1,left,right)
    def que(self,ind,low,high,left,right):
        
        #Complete overlap
        if left<=low<=high<=right:
            return self.seg[ind]

        #Partial overlap
        if low<=left<=high or low<=right<=high:
            mid=(low+high)//2
            return self.merge(self.que(2*ind+1,low,mid,left,right),self.que(2*ind+2,mid+1,high,left,right))

        #No overlap
        if right<low or high<left:
            return self.default

    def __repr__(self):
        return f'SegmentTree([{', '.join(map(str,[self.query(i,i) for i in range(1,self.n+1)]))}])'


#Without yield
class LazySegmentTree:

    def __init__(self,l,merge,default):
        self.merge=merge
        self.default=default
        self.n=1<<len(l).bit_length() if len(l)&(len(l)-1) else len(l)
        self.seg=[self.default for i in range(2*self.n)]
        self.lazy=[0]*(2*self.n)
        for i in range(self.n,2*self.n):
            if i-self.n>=len(l):
                break
            else:
                self.seg[i]=l[i-self.n]
        for ind in range(self.n-1,0,-1):
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1-based indexing (Val to be added)
    def update(self,left,right,val):
        return self.upd(1,0,self.n-1,left-1,right-1,val)

    def upd(self,ind,low,high,left,right,val):
        
        self.pull(ind,low,high)
            
        #Complete overlap
        if left<=low<=high<=right:
            self.push(ind,low,high,val)

        #Partial overlap
        elif low<=left<=high or low<=right<=high:
            mid=(low+high)//2
            self.upd(2*ind,low,mid,left,right,val)
            self.upd(2*ind+1,mid+1,high,left,right,val)
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1-based indexing
    def query(self,left,right):
        return self.que(1,0,self.n-1,left-1,right-1)

    def que(self,ind,low,high,left,right):

        self.pull(ind,low,high)

        #Complete overlap
        if left<=low<=high<=right:
            return self.seg[ind]

        #Partial overlap
        if low<=left<=high or low<=right<=high:
            mid=(low+high)//2
            return self.merge(self.que(2*ind,low,mid,left,right),self.que(2*ind+1,mid+1,high,left,right))

        #No overlap
        if right<low or high<left:
            return self.default

    def pull(self,ind,low,high):
        if self.lazy[ind]!=0:
            self.seg[ind]+=(high-low+1)*self.lazy[ind]  #Change as needed
            if low!=high:
                self.lazy[2*ind]+=self.lazy[ind]
                self.lazy[2*ind+1]+=self.lazy[ind]
            self.lazy[ind]=0

    def push(self,ind,low,high,val):
        self.seg[ind]+=(high-low+1)*val             #Change as needed
        if low!=high:
            self.lazy[2*ind]+=val
            self.lazy[2*ind+1]+=val

    def __repr__(self):
        return f'SegmentTree([{', '.join(map(str,[self.query(i,i) for i in range(1,self.n+1)]))}])'

def solve():
    global seg,l,lazy,n
    n=int(input())
    l=list(map(int,input().split()))
    seg=LazySegmentTree(l,max,0)
    q=int(input())
    for i in range(q):
        ty,left,right=map(int,input().split())
        if ty==1:
            print(seg.query(left,right))
        else:
            val=int(input())
            seg.update(left,right,val)
        
for _ in range(int(input())):
    solve()

'''
1
10
3 6 8 3 7 9 4 1 10 2
100
'''
