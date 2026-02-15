class DSU:
    
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(self.n+1)]
        self.size=[1 for i in range(self.n+1)]
 
    def find(self,node):
        stk=[]
        while not node==self.par[node]:
            stk.append(node)
            node=self.par[node]
        while stk:
            self.par[stk.pop()]=node
        return node
        '''
        if node==self.par[node]:
            return node
        else:
            self.par[node]=self.find(self.par[node])
            return self.par[node]
        '''

    def connected(self,node1,node2):
        return self.find(node1)==self.find(node2)
     
    def Union(self,node1,node2):
        node1=self.find(node1)
        node2=self.find(node2)
        if node1!=node2:
            if self.size[node1]<self.size[node2]:
                node1,node2=node2,node1
            self.par[node2]=node1
            self.size[node1]+=self.size[node2]

    def group_heads(self):
        return [i for i in range(1,self.n+1) if self.par[i]==i]

    def groups_with_members(self):
        groups=[[] for i in range(self.n+1)]
        for i in range(1,self.n+1):
            groups[self.find(i)].append(i)
        return groups
