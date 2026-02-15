'''
Centroid of a Tree: It is that node, which when removed, divides the tree into
subtrees each having size less than or equal to N//2.

Properties of a Centroid Tree:
-> It contains all (N) nodes of the original tree.
-> The height of a centroid tree is at most log(N).
-> Consider any two arbitrary vertices A and B. The path between
   them (in original tree) can be broken down into A->C and C->B
   where C is LCA of A and B in centroid tree.
-> Hence, we decompose the given tree into NlogN different paths
   (from each centroid to all the vertices in the corresponding
   part) such that any path is a concatenation of two different
   paths from this set.  
'''

class CentroidDecomposition:

    def __init__(self,n):
        self.n=n
        self.U,self.V,self.W,self.deleted=[0]*n,[0]*n,[0]*n,[0]*n
        self.adj=[[] for i in range(n+1)]
        self.par=[0]*(n+1) #for centroid tree
        self.level=[0]*(n+1) #for centroid tree
        for edge_no in range(1,n):
            u,v,w=map(int,input().split())
            self.U[edge_no]=u
            self.V[edge_no]=v
            self.W[edge_no]=w
            self.adj[u].append(edge_no)
            self.adj[v].append(edge_no)
        self.dist=[[0]*(n+1)]
        self.dfs_for_sub(1,0)
        stk=[]
        stk.append((1,0))
        while stk:
            parent,grand_par=stk.pop()
            centroid=self.find_centroid(parent)
            if grand_par:
                self.par[centroid]=grand_par
                self.level[centroid]=self.level[grand_par]+1
            self.centroidDist(centroid,centroid,self.level[centroid])
            for edge_no in self.adj[centroid]:
                child=self.U[edge_no]^self.V[edge_no]^centroid
                if not self.deleted[edge_no]:
                    self.deleted[edge_no]=1
                    stk.append((child,centroid))

    def dfs_for_sub(self,parent,grand_par):
        tra=[]
        stks=[]
        stks.append((parent,grand_par))
        self.sub=[1]*(n+1)
        self.sub[0]=0
        while stks:
            parent,grand_par=stks.pop()
            tra.append((parent,grand_par))
            for edge_no in self.adj[parent]:
                child=self.U[edge_no]^self.V[edge_no]^parent
                if child!=grand_par and not self.deleted[edge_no]:
                    stks.append((child,parent))
        for child,parent in tra[::-1]:
            if parent==0:
                continue
            self.sub[parent]+=self.sub[child]
            
    def find_centroid(self,parent):
        stkc=[]
        stkc.append(parent)
        while stkc:
            parent=stkc.pop()
            limit=self.sub[parent]>>1
            f=1
            for edge_no in self.adj[parent]:
                child=self.U[edge_no]^self.V[edge_no]^parent
                if not self.deleted[edge_no] and self.sub[child]>limit:
                    stkc.append(child)
                    #Rerooting
                    self.sub[parent]-=self.sub[child]
                    self.sub[child]+=self.sub[parent]
                    f=0
                    break
            if f:
                return parent

    def centroidDist(self,parent,grand_par,lvl):
        #dist[lvl][node]:Keeps the distance from that level to the nodes of its subtree
        stkd=[]
        if len(self.dist)==lvl:
            self.dist.append([0]*(n+1))
        stkd.append((parent,grand_par))
        while stkd:
            parent,grand_par=stkd.pop()
            for edge_no in self.adj[parent]:
                child=self.U[edge_no]^self.V[edge_no]^parent
                if child!=grand_par and not self.deleted[edge_no]:
                    self.dist[lvl][child]=self.dist[lvl][parent]+self.W[edge_no]
                    stkd.append((child,parent))

    def lca(self,node1,node2):
        while node1!=node2:
            if self.level[node1]<self.level[node2]:
                node2=self.par[node2]
            elif self.level[node1]>self.level[node2]:
                node1=self.par[node1]
            else:
                node1=self.par[node1]
                node2=self.par[node2]
        return node1

    def distance(self,node1,node2):
        LCA=self.lca(node1,node2)
        lvl=self.level[LCA]
        return self.dist[lvl][node1]+self.dist[lvl][node2]

n=int(input())
cd=CentroidDecomposition(n)
print('par',cd.par)
print('level',cd.level)
print('dist',cd.dist)
'''
15
1 2 1
3 2 2
4 2 1
2 5 2
5 6 1
6 7 2
5 8 1
8 9 2
9 10 1
10 11 2
10 12 1
9 13 2
13 14 1
13 15 2
'''

'''
par [0, 2, 8, 2, 2, 6, 2, 6, 0, 8, 9, 10, 10, 9, 13, 13]
level [0, 2, 1, 2, 2, 3, 2, 3, 0, 1, 2, 3, 3, 2, 3, 3]
'''
