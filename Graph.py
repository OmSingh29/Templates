#from math import *
from collections import *
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

def vis(a):
    #v_a=visited array defined globally and a is the number with smallest value 1
    if v_a[a-1]==1:
        return True
    else:
        return False

def bfs(root):
    vis=[0]*(n+1)
    lvl=[0]*(n+1)
    que=deque()
    que.appendleft(root)
    lvl[root]=0
    vis[root]=1
    while que:
        par=que.pop()
        for child in adj[par]:
            if not vis[child]:
                que.appendleft(child)
                lvl[child]=lvl[par]+1
                vis[child]=1
                
def dfs(a):
    #a is the root node for traversal (a>0)
    #graph is the name of adjacency list representation of graph
    temp=adj_list[a-1]
    v_a[a-1]=1
    #tra.append(a)
     
    for i,j in enumerate(temp):
        if not vis(j):
            dfs(j)

def solve():
    global v,e,v_a,adj_list,tra
    #v=int(input())
    v,e=map(int,input().split())
    v_a=[0]*v
    adj_list=[[] for i in range(v)]
    for i in range(e):
        x,y=map(int,input().split())
        adj_list[x-1].append(y)
        adj_list[y-1].append(x)
    tra=[]
    bfs(1)
    out(tra)

for _ in range(int(input())):
    solve()

'''
1
13 12
1 2
2 5
5 6
5 7
5 8
8 12
1 3
3 4
4 9
4 10
10 11
1 13
'''
