def exclusive(A,zero,combine,node):
    n=len(A)
    exclusiveA=[zero]*n # Exclusive segment tree
 
    # Build exclusive segment tree
    for bit in range(n.bit_length())[::-1]:
        for i in range(n)[::-1]:
            # Propagate values down the segment tree    
            exclusiveA[i]=exclusiveA[i//2]
        for i in range(n&~int(bit==0)):
            # Fold A[i] into exclusive segment tree
            ind=(i>>bit)^1
            exclusiveA[ind]=combine(exclusiveA[ind],A[i],node,i)
    return exclusiveA
 
def rerooter(graph,default,combine,finalize):
    n=len(graph)
    rootDP=[0]*n
    forwardDP=[None]*n
    reverseDP=[None]*n
 
    # Compute DP for root=0
    DP=[0]*n
    bfs=[0]
    P=[0]*n
    for parent in bfs:
        for child in graph[parent]:
            if P[parent]!=child:
                P[child]=parent
                bfs.append(child)
 
    for parent in reversed(bfs):
        parentDP=default[parent]
        for eind,child in enumerate(graph[parent]):
            if P[parent]!=child:
                parentDP=combine(parentDP,DP[child],parent,eind)
        DP[parent]=finalize(parentDP,parent,graph[parent].index(P[parent]) if parent else -1)
    # DP for root=0 done
    
    # Use the exclusive function to reroot 
    for parent in bfs:
        DP[P[parent]]=DP[parent]
        forwardDP[parent]=[DP[child] for child in graph[parent]]
        rerootDP=exclusive(forwardDP[parent],default[parent],combine,parent)
        reverseDP[parent]=[finalize(nodeDP,parent,eind) for eind,nodeDP in enumerate(rerootDP)]
        rootDP[parent]=finalize((combine(rerootDP[0],forwardDP[parent][0],parent,0) if n>1 else default[parent]),parent,-1)
        for child,dp in zip(graph[parent],reverseDP[parent]):
            DP[child]=dp
    return rootDP,forwardDP,reverseDP
 
def combine(parentDP,childDP,parent,eind):
    '''
    Never change parentDP in place
    '''
    pass
 
def finalize(parentDP,parent,eind):
    '''
    Never change parentDP in place
    '''
    pass

#default=[0]*n
#rootDP,forwardDP,reverseDP=rerooter(adj,default,combine,finalize)
#out(rootDP)
