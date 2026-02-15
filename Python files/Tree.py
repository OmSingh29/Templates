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

'''
for 3rd parameter whose no. of bits taken in binary representation is atmost 3
ele=heappop(h)
wt,parent,step=ele>>23,(ele&(0xfffff<<3))>>3,ele&((1<<3)-1)
'''
'''
ele=heappop(h)
wt,x,y=ele>>40,(0xfffff00000&ele)>>20,0xfffff&ele   #Will work for 0<=x<=10**6,0<=y<=10**6
'''
def dijkstra(source,dest=-1):
    #Returns -1 if no path is found
    func=lambda u,v:u<<20^v
    h=[]
    heappush(h,func(0,source))   #0 is weight and source is point from where it starts
    dist=[float('inf')]*(n+1)
    dist[source]=0
    while h:
        wt,parent=h[0]>>20,heappop(h)&0xfffff
        if dist[parent]!=wt:
            continue
        if parent==dest:
            return dist[parent]
        for child,wt in adj[parent]:
            if dist[child]>dist[parent]+wt:
                dist[child]=dist[parent]+wt
                heappush(h,func(dist[child],child))
    return dist if dest==-1 else -1

def getPath(src,dest):
    node=dest
    path=[]
    while node!=src:
        path.append(node)
        node=par[node]
    path.append(src)
    return path[::-1]

def diameter_of_tree():

    def bfs(root):
        lvl=[0]*(n+1)
        ma=0
        node=root
        que=deque()
        que.appendleft((root,0))
        while que:
            parent,grand_par=que.pop()
            for child in adj[parent]:
                if child!=grand_par:
                    que.appendleft((child,parent))
                    lvl[child]=lvl[parent]+1
                    if ma<lvl[child]:
                        ma=lvl[child]
                        node=child
        return ma,node

    from collections import deque
    ma,node1=bfs(1)
    dia,node2=bfs(node1)
    return dia,node1,node2

def bfs(root):
    '''
    lvl=[float('inf')]*(n+1)
    lvl[root]=0   #Assign it correctly (Maybe going to root node isn't possible)
    vis=[0]*(n+1)
    vis[root]=1
    par=[0]*(n+1)
    tra=[]
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
                vis[child]=1
                lvl[child]=lvl[parent]+1
                par[child]=parent
                '''

def dfs(parent,grand_par=0):
    #tra.append(par)
    for child in adj[parent]:
        if child!=grand_par:
            #dpth[child]=dpth[parent]+1
            #dist[child]=dist[parent]+w
            dfs(child,parent)
            #hght[parent]=max(hght[parent],hght[child]+1)
            #sub[parent]+=sub[child]

def iter_dfs(root):
    tra=[]
    stk=[]
    stk.append((root,0))
    sub=[1]*(n+1)
    sub[0]=0
    vis=[False]*(n+1)
    #done=[False]*(n+1)   #Required if its not a tree, used in backtracking part
    while stk:
        parent,grand_par=stk[-1]
        if vis[parent]:
            #Backtracking part
            for child in adj[parent]:
                if done[child]:
                    pass
            done[parent]=True
        else:
            vis[parent]=True
            if grand_par:
                pass
            for child in adj[parent]:
                stk.append((child,parent))

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
