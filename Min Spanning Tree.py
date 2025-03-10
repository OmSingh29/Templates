#from math import *
#from collections import *
#from bisect import *
from heapq import heappush,heappop
#from random import *

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)

def out(l):
    print('\n'.join(map(str,l)))

def yes():
    print('Yes')

def no():
    print('No')

def alice():
    print('Alice')

def bob():
    print('Bob')

def func(u,v,w):
    return (u<<40)^(v<<20)^w 

def prims():
    vis=[0]*(v+1)
    dist=[float('inf')]*(v+1)
    h=[]
    heappush(h,func(0,0,0))
    dist[0]=0
    while h:
        ele=heappop(h)
        wt,x,y=ele>>40,(0xfffff00000&ele)>>20,0xfffff&ele   #0<=wt<inf 0<=x<=10**6 0<=y<=10**6
        if wt!=dist[x]:
            continue
        '''if y!=x:
            edge.append((x,y))'''  #gives you the edges of min spanning tree
        vis[x]=1
        for wt,node in adj[x]:
            if not vis[node] and wt<dist[node]:
                dist[node]=wt
                heappush(h,func(wt,node,x))

def solve():
    global v,e,adj,dist,edge
    edge=[] 
    #v=int(input())
    v,e=map(int,input().split())
    adj=[[] for i in range(v+1)]
    for i in range(e):
        x,y,wt=map(int,input().split())
        adj[x].append((wt,y))
        adj[y].append((wt,x))
    prims()
  
for _ in range(1):
    solve()

'''
6 9
5 4 9
1 4 1
5 1 4
4 3 5
4 2 3
1 2 2
3 2 3
3 6 8
2 6 7
'''
