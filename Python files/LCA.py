class LowestCommonAncestor:

    def __init__(self,root,adj):
        self.adj=adj
        self.n=len(adj)-1
        self.bfs(root)
        self.ancestor=[]
        self.ancestor.append(self.par)
        k=2     #kth ancestor
        while k<=self.n:
            kth_ancestor=[]
            last=self.ancestor[-1]
            for node in range(self.n+1):   #of each element of parent list
                kth_ancestor.append(last[last[node]])
            self.ancestor.append(kth_ancestor)
            k<<=1

    def bfs(self,root):
        self.lvl=[0]*(self.n+1)
        self.par=[0]*(self.n+1)
        from collections import deque
        que=deque()
        que.appendleft((root,-1))
        while que:
            parent,grand_par=que.pop()
            for child in self.adj[parent]:
                if child!=grand_par:
                    que.appendleft((child,parent))
                    self.lvl[child]=self.lvl[parent]+1
                    self.par[child]=parent
                    
    #Returns 0 if kth ancestor doesn't exist
    def kth_anc(self,node,k):
        ans=node
        bit=0
        while k:
            if k%2:
                ans=self.ancestor[bit][ans]
            bit+=1
            k>>=1
        return ans
    
    def lca(self,node1,node2):
        d1=self.lvl[node1]
        d2=self.lvl[node2]
        if d1>d2:
            node1=self.kth_anc(node1,d1-d2)
        elif d1<d2:
            node2=self.kth_anc(node2,d2-d1)
        if node1==node2:
            return node1
        mini=min(d1,d2)
        mask=1
        bit=0
        while mask*2<=mini:
            mask*=2
            bit+=1
        while mask:
            justbelow1=self.ancestor[bit][node1]
            justbelow2=self.ancestor[bit][node2]
            if justbelow1!=justbelow2:
                node1=justbelow1
                node2=justbelow2
            mask>>=1
            bit-=1
        return self.par[node1]
