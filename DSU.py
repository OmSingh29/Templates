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

class DSU:
    def __init__(self,v):
        global par,size
        par=[i for i in range(v+1)]
        size=[1 for i in range(v+1)]

    def find(self,node):
        stk=[]
        while not node==par[node]:
            stk.append(node)
            node=par[node]
        for i in stk:
            par[i]=node
        return node
        '''if node==par[node]:
            return node
        else:
            par[node]=self.find(par[node])
            return par[node]'''
     
    def Union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if size[a]<size[b]:
                a,b=b,a
            par[b]=a
            size[a]+=size[b]
            return 1
        else:
            return 0

def solve():
    v=int(input())
    #v,e=map(int,input().split())
    par=[]
    size=[]
    dsu=DSU(v)
        
for _ in range(int(input())):
    solve()
