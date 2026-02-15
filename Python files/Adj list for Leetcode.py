#val for Leetcode
#data for gfg
#call it as self.createadj(root)
def createadj(self,root):
    adj=defaultdict(list)
    q=deque()
    q.appendleft(root)
    adj[root.data]=[]
    while q:
        par=q.pop()
        if par.left:
            q.appendleft(par.left)
            adj[par.data].append(par.left.data)
            adj[par.left.data].append(par.data)
        if par.right:
            q.appendleft(par.right)
            adj[par.data].append(par.right.data)
            adj[par.right.data].append(par.data)
    return adj
