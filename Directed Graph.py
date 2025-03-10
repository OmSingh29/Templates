#from math import ceil,log,lcm,gcd,isfinite
from collections import deque,Counter,defaultdict
#from bisect import bisect
#from heapq import heappush,heappop
#from fractions import Fraction as fr
#from sortedcontainers import SortedList,SortedSet,SortedDict
#from random import randint

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)

def detectCycle(par):
    vis[par]=1
    path_vis[par]=1
    for child in adj[par]:
        if not vis[child]:
            if detect_cycle(child):
                return True
        elif path_vis[child]:
            return True
    path_vis[par]=0
    return False

def dijkstra(src):
    dist=[float('inf')]*(n+1)
    dist[src]=0
    for par in topo:
        for child,wt in adj[par]:
            dist[child]=min(dist[child],dist[par]+wt)
    return dist

#Topological Sort:Linear ordering of vertices such that if there is an edge from u to v
#then u comes before v
#Only for directed acyclic graph
#You can also use it for directed cyclic graph (it will automatically end when it sees a cycle because indeg[i]!=0)
def topoSort():
    indeg=[0]*(n+1)
    for l in adj:
        for child in l:
            indeg[child]+=1
    #lvl=[0]*(n+1)
    q=deque()
    for i,j in enumerate(indeg):
        if i and not j:
            q.appendleft(i)
            #lvl[i]=1
    topo=[]
    #sub=[0]*(n+1)
    #mark=[0]*(n+1)
    while q:
        parent=q.pop()
        topo.append(parent)
        #sub[parent]+=1
        #mark[parent]=1
        for child in adj[parent]:
            indeg[child]-=1
            #sub[child]+=sub[parent]
            if not indeg[child]:
                q.appendleft(child)
                #lvl[child]=lvl[parent]+1
    '''for i,j in enumerate(mark):
        if not j:
            sub[i]=0'''
    return topo

def solve():
    global vis,path_vis,adj,n
    n,e=map(int,input().split())
    vis=[0]*(n+1)
    path_vis=[0]*(n+1)
    adj=[[] for i in range(n+1)]
    for i in range(e):
        x,y=map(int,input().split())
        adj[x].append(y)
    print(topoSort())

for _ in range(1):
    solve()
