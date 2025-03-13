class LowComAnc():

    def __init__(self,root,adj):
        self.adj=adj
        self.bfs(root)
        self.ancestor=[]
        self.ancestor.append(self.par)
        k=2     #kth ancestor
        while k<=n:
            kth_ancestor=[]
            last=self.ancestor[-1]
            for node in range(n+1):   #of each element of parent list
                kth_ancestor.append(last[last[node]])
            self.ancestor.append(kth_ancestor)
            k<<=1

    def bfs(self,root):
        self.lvl=[0]*(n+1)
        self.par=[0]*(n+1)
        que=deque()
        que.appendleft((root,-1))
        while que:
            parent,grand_par=que.pop()
            for child in self.adj[parent]:
                if child!=grand_par:
                    que.appendleft((child,parent))
                    self.lvl[child]=self.lvl[parent]+1
                    self.par[child]=parent

    def kth_anc(self,node,k):
        ans=node
        i=0
        while k:
            if k%2:
                ans=self.ancestor[i][ans]
            i+=1
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
        k=1
        mi=min(d1,d2)
        while k*2<=mi:
            k*=2
        while k:
            justbelow1=self.kth_anc(node1,k)
            justbelow2=self.kth_anc(node2,k)
            if justbelow1!=justbelow2:
                node1=justbelow1
                node2=justbelow2
            k>>=1
        return self.par[node1]
