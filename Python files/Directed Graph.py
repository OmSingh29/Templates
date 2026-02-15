'''
Some tips for Directed Graph
1. If you want to check whether a path exists or not between two nodes,simply use bfs
2. If len(topo)!=n, graph is cyclic.
3. If you want to have minimum or maximum levels, use toposort.
    (Both min and max can be done using toposort)
'''

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
    from collections import deque
    q=deque()
    for i,j in enumerate(indeg):
        if i and not j:
            q.appendleft(i)
            #lvl[i]=1
    topo=[]
    while q:
        parent=q.pop()
        topo.append(parent)
        for child in adj[parent]:
            indeg[child]-=1
            #If you want to have constraints on path, do it from here (dont continue)
            if not indeg[child]:
                q.appendleft(child)
                #lvl[child]=lvl[parent]+1
    return topo

def dijkstra(src):
    topo=topoSort()
    dist=[float('inf')]*(n+1)
    dist[src]=0
    for par in topo:
        for child,wt in adj[par]:
            dist[child]=min(dist[child],dist[par]+wt)
    return dist

def topoSortfrom(roots):
    from collections import deque
    vis=[0]*(n+1)
    q=deque()
    for root in roots:
        q.appendleft(root)
        vis[root]=1
    #Checking which nodes we can visit starting from these roots
    while q:
      parent=q.pop()
      for child in adj[parent]:
        if not vis[child]:
          vis[child]=1
          q.appendleft(child)
    indeg=[0]*(n+1)
    for i,l in enumerate(adj):
        if not vis[i]:
            continue
        for child in l:
            indeg[child]+=1
    #lvl=[0]*(n+1)
    q=deque()
    for i,j in enumerate(indeg):
        if i and not j and vis[i]:
            q.appendleft(i)
            #lvl[i]=1
    topo=[]
    while q:
        parent=q.pop()
        topo.append(parent)
        for child in adj[parent]:
            indeg[child]-=1
            #Continue from here if needed
            if not indeg[child]:
                q.appendleft(child)
                #lvl[child]=lvl[parent]+1
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
