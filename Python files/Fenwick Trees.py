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

class BIT:
    #fen[i] stores the sum from i-(i&-i)+1 to i
    #i&-i gives you the value of last set bit in binary representation of i
    def __init__(self,l):
        self.n=len(l)
        self.fen=[0]*(self.n+1)
        pre=[0]
        for i in range(self.n):
            pre.append(pre[-1]+l[i])
        for i in range(1,self.n+1):
            self.fen[i]=pre[i]-pre[i-(i&-i)]

    # 1 based indexing
    def update(self,ind,val):
        while ind<=self.n:
            self.fen[ind]+=val
            ind+=(ind&-ind)

    # 1 based indexing
    def query(self,ind):
        ans=0
        while ind:
            ans+=self.fen[ind]
            ind-=(ind&-ind)
        return ans

def solve():
    global n,l,fen
    n=int(input())
    #s=input()
    #x,y=map(int,input().split())
    l=list(map(int,input().split()))
    obj=BIT(l)
    q=int(input())
    for i in range(q):
        ty=int(input())
        if ty==1:
            ind=int(input())
            print(obj.query(ind))
        else:
            ind,val=map(int,input().split())
            obj.update(ind,val-l[ind-1])
            l[ind-1]=val
        
for _ in range(int(input())):
    solve()
