from math import ceil,log
from collections import deque,Counter
#from bisect import bisect
from heapq import heappush,heappop
#from random import randint

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

def preCom_ancestors():
    global ancestor
    ancestor=[]
    ancestor.append(par)
    k=2     #kth ancestor
    while k<=n:
        kth_ancestor=[]
        last=ancestor[-1]
        for node in range(n+1):   #of each element of parent list
            kth_ancestor.append(last[last[node]])
        ancestor.append(kth_ancestor)
        k<<=1

def kth_anc(node,k):
    ans=node
    i=0
    while k:
        if k%2:
            ans=ancestor[i][ans]
        i+=1
        k>>=1
    return ans

def lca(node1,node2):
    d1=lvl[node1]
    d2=lvl[node2]
    if d1>d2:
        node1=kth_anc(node1,d1-d2)
    elif d1<d2:
        node2=kth_anc(node2,d2-d1)
    if node1==node2:
        return node1
    k=1
    while k*2<=min(d1,d2):
        k*=2
    while k:
        justbelow1=kth_anc(node1,k)
        justbelow2=kth_anc(node2,k)
        if justbelow1!=justbelow2:
            node1=justbelow1
            node2=justbelow2
        k>>=1
    return par[node1]

def isBipartite(root):
    vis=[0]*(n+1)
    bip=[-1]*(n+1)
    que=deque()
    que.appendleft((root,0))
    vis[root]=1
    while que:
        parent,grand_par=que.pop()
        for child in adj[parent]:
            if not vis[child]:
                if bip[child]==-1:
                    bip[child]=bip[parent]^1
                    que.appendleft((child,parent))
                    vis[child]=1
                elif bip[child]==bip[parent]:
                    return False
    return True

def func(u,v,w):
    return (u<<22)^(v<<3)^w

def func(u,v,w):
    return (u<<40)^(v<<20)^w

def func(u,v):
    return u<<20^v

def dijkstra(source):
    h=[]
    heappush(h,func(0,source))   #0 is weight and source is point from where it start
    dist=[float('inf')]*(n+1)
    dist[source]=0
    while h:
        wt,par=h[0]>>20,heappop(h)&0xfffff
        '''
        for 3rd parameter whose no. of bits taken in binary representation is atmost 3
        ele=heappop(h)
        wt,par,step=ele>>23,(ele&(0xfffff<<3))>>3,ele&((1<<3)-1)
        '''
        '''
        ele=heappop(h)
        wt,x,y=ele>>40,(0xfffff00000&ele)>>20,0xfffff&ele   #Will work for 0<=x<=10**6,0<=y<=10**6
        '''
        if dist[par]!=wt:
            continue
        for child,wt in adj[par]:
            if dist[child]>dist[par]+wt:
                dist[child]=dist[par]+wt
                heappush(h,func(dist[child],child))
    return dist

def getPath(src,dest):
    node=dest
    path=[]
    while node!=src:
        path.append(node)
        node=par[node]
    path.append(src)
    return path

def diameter():
    ma,node1=bfs(1)
    dia,node2=bfs(node1)
    return dia,node1,node2

def bfs(root):
    '''
    tra=[]
    lvl=[0]*(n+1)
    vis=[0]*(n+1)
    par=[0]*(n+1)
    ma=float('-inf')
    '''
    que=deque()
    que.appendleft((root,-1))
    while que:
        parent,grand_par=que.pop()
        #tra.append(parent)
        for child in adj[parent]:
            if child!=grand_par:
                que.appendleft((child,parent))
                '''
                lvl[child]=lvl[parent]+1
                par[child]=parent
                if ma<lvl[child]:
                    ma=lvl[child]
                    node=child
    return ma,node
    '''

def dfs(par,grand_par=0):
    #tra.append(par)
    for child in adj[par]:
        if child!=grand_par:
            #dpth[child]=dpth[par]+1
            dfs(child,par)
            #hght[par]=max(hght[par],hght[child]+1)

def iter_dfs(root):
    tra=[]
    stk=[]
    stk.append((root,0))
    while stk:
        parent,grand_par=stk.pop()
        tra.append((parent,grand_par))
        for child in adj[parent]:
            if child!=grand_par:
                #dpth[child-1]=dpth[par-1]+1
                stk.append((child,parent))
    for child,parent in tra[::-1]:
        if parent==0:
            continue
        '''
        hght[par]=max(hght[par],hght[child]+1)
        #Leaf nodes have 0 height
        '''

def solve():
    global v,e,adj,tra,hght,dpth,par,lvl,dist,size,par_dsu,sub
    #v=int(input())
    v,e=map(int,input().split())
    v_a=[0]*(v+1)
    adj=[[] for i in range(v+1)]
    for i in range(e):
        x,y,w=map(int,input().split())
        adj[x].append((y,w))
        adj[y].append((x,w))
    dist=[float('inf')]*(v+1)
    dijkstra(1)
    print(dist)
    '''tra=[]
    hght=[0]*v
    dpth=[0]*v
    lvl=[0]*v
    par_list=[0]*v
    dfs(1)
    out(tra)
    print('Heights are:')
    out(hght)
    print('Depths are:')
    out(dpth)
    print('Levels are:')
    out(lvl)
    #out(lvl)
    #dfs(1)
    #preCom_kth_anc()
    #kanc=kth_anc(node,k)
    #lca(n1,n2)
    '''
    
    #For calculating diameter of tree
    '''
    max_dpth=float('-inf')
    for i,j in enumerate(dpth):
        if max_dpth<j:
            max_dpth=j
            node=i+1
        dpth[i]=0
    dfs(node)
    dia=max(dpth)
    print(dia)
    '''

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
