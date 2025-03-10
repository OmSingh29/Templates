#from math import *
#from collections import *
#from bisect import *
#from heapq import *

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)

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

def build(ind,low,high):
    if low==high:
        seg[ind]=l[low]
        return
    mid=(low+high)//2
    build(2*ind+1,low,mid)
    build(2*ind+2,mid+1,high)
    seg[ind]=seg[2*ind+1]+seg[2*ind+2]

def update(ind,low,high,i,val):
    if low==high==i:
        seg[ind]=val
        return
    mid=(low+high)//2
    if low<=i<=high:
        if i<=mid:
            update(2*ind+1,low,mid,i,val)
        else:
            update(2*ind+2,mid+1,high,i,val)
        seg[ind]=min(seg[2*ind+1],seg[2*ind+2])

def query(ind,low,high,left,right):
    mid=(low+high)//2
    # seg[ind] stores the required sum/max/min of range[low,high]
    #Complete overlap
    if left<=low<=high<=right:
        return seg[ind]

    #Partial overlap
    if low<=left<=high or low<=right<=high:
        a=query(2*ind+1,low,mid,left,right)
        b=query(2*ind+2,mid+1,high,left,right)
        return min(a,b)

    #No overlap
    if right<low or high<left:
        return float('inf')

def update_range(ind,low,high,left,right,val):
    if lazy[ind]!=0:
        seg[ind]+=((high-low+1)*lazy[ind])
        if low!=high:
            lazy[2*ind+1]+=lazy[ind]
            lazy[2*ind+2]+=lazy[ind]
        lazy[ind]=0

    mid=(low+high)//2
    #Complete overlap
    if left<=low<=high<=right:
        seg[ind]+=(high-low+1)*val
        if low!=high:
            lazy[2*ind+1]+=val
            lazy[2*ind+2]+=val
        return

    #Partial overlap
    if low<=left<=high or low<=right<=high:
        update_range(2*ind+1,low,mid,left,right,val)
        update_range(2*ind+2,mid+1,high,left,right,val)
        seg[ind]=seg[2*ind+1]+seg[2*ind+2]
        return

    #No overlap
    if right<low or high<left:
        return

def query_range(ind,low,high,left,right):
    if lazy[ind]!=0:
        seg[ind]+=((high-low+1)*lazy[ind])
        if low!=high:
            lazy[2*ind+1]+=lazy[ind]
            lazy[2*ind+2]+=lazy[ind]
        lazy[ind]=0

    mid=(low+high)//2
    #Complete overlap
    if left<=low<=high<=right:
        return seg[ind]

    #Partial overlap
    if low<=left<=high or low<=right<=high:
        a=query_range(2*ind+1,low,mid,left,right)
        b=query_range(2*ind+2,mid+1,high,left,right)
        return a+b

    #No overlap
    if right<low or high<left:
        return 0

def solve():
    global seg,l,lazy,n
    n=int(input())
    l=list(map(int,input().split()))
    seg=[0]*(4*n)
    lazy=[0]*(4*n)
    build(0,0,n-1)
    out(seg)
    q=int(input())
    for i in range(q):
        ty,left,right=map(int,input().split())
        if ty==1:
            print(query_range(0,0,n-1,left-1,right-1))
        else:
            val=int(input())
            update_range(0,0,n-1,left-1,right-1,val)
        
for _ in range(int(input())):
    solve()

'''
1
10
3 6 8 3 7 9 4 1 10 2
'''
