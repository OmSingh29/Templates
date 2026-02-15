from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

'''
vis=[0]*(v+1)
art=[0]*(v+1)
min_step=[0]*(v+1)
tin=[0]*(v+1)
'''

@bootstrap
def articulation_point(timer,parent,grand_par=0):
    vis[parent]=True
    lowest_time[parent]=tin[parent]=timer
    non_vis_child=0
    for child in adj[parent]:
        if child==grand_par:
            continue
        if not vis[child]:
            yield articulation_point(timer+1,child,parent)
            lowest_time[parent]=min(lowest_time[parent],lowest_time[child])
            if grand_par and timer<=lowest_time[child]:
                articulation[parent]=1
            non_vis_child+=1
        else:
            lowest_time[parent]=min(lowest_time[parent],tin[child])
    if not grand_par and non_vis_child>1:
        articulation[parent]=1
    yield


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


'''DSU'''
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

#Returns all prime numbers in the range [start>=1,end]
def range_sieve(start,end):
    #Calculate primes till sqrt(n)
    global mark,isprime,primes
    n=int(pow(end,0.5))
    mark,primes=[True]*(n+1),[]
    mark[0]=mark[1]=False
    for i in range(2,n+1):
        if not mark[i]:
            continue
        primes.append(i)
        for j in range(i*i,n+1,i):
            mark[j]=False
    #Using marked primes to get primes in [start,end]
    isprime=[True]*(end-start+1)
    if start==1:
        isprime[0]=False
    for i in primes:
        num=(start-1)-((start-1)%i)
        for j in range(max(i*i,num+i),end+1,i):
            isprime[j-start]=False

def calculate_sum(n):
    '''
    Returns sum of digits from 1 to n in O(log(n))
    '''
    nn=n
    ans=0
    coeff=1
    while nn:
        j=nn%10
        quo=n//(coeff*10)
        rem=n%coeff
        ans+=45*coeff*quo
        ans+=j*(j-1)//2*coeff
        ans+=j*(rem+1)
        coeff*=10
        nn//=10
    return ans

# Miller-Rabin primality test O((log(n))**3)
def is_prime(n,k=5):  # number of tests
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0:
        return False
 
    # write n-1 as 2^r * d
    r,d =0,n-1
    while d%2==0:
        d//=2
        r+=1
 
    # witness loop
    from random import randrange
    for _ in range(k):
        a=randrange(2,n-1)
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        for _ in range(r-1):
            x=pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True

def intersectIntervals(intervals1,intervals2):
    intervals1.sort()
    intervals2.sort()
    answer=[]
    i,j=0,0
    while i<len(intervals1) and j<len(intervals2):
        start=max(intervals1[i][0],intervals2[j][0])
        end=min(intervals1[i][1],intervals2[j][1])
        if start<=end:
            answer.append((start,end))
        if intervals1[i][1]<intervals2[j][1]:
            i+=1
        else:
            j+=1
    return answer

'''LCA'''
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

#Time Complexity: O(26*n) => O(n)
#Returns empty string if k>valid permutations
def lexicographically_kth_string(s,k):
    def nCr(n,r,limit):
        if n<r or r<0:
            return 0
        r=min(r,n-r)
        ans=1
        for i in range(1,r+1):
            ans*=n-i+1
            ans//=i
            if ans>limit:
                return limit+1
        return ans

    def permutation(st):
        tot=1
        pos=n-st
        for i,j in enumerate(cnt):
            if not j:
                continue
            tot*=nCr(pos,j,k)
            if tot>k:
                return tot
            pos-=j
        return tot

    n=len(s)
    cnt=[0]*26
    for j in s:
        cnt[ord(j)-ord('a')]+=1
    char=[]
    for i,j in enumerate(cnt):
        if j:
            char.append(chr(ord('a')+i))
    st=0
    tot=permutation(0)
    if tot<k:
        return ''
    ans=[]
    while True:
        new=[]+char
        for ch in char:
            ind=ord(ch)-ord('a')
            cnt[ind]-=1
            tot=permutation(st+1)
            if tot>=k:
                ans.append(ch)
                st+=1
                if cnt[ind]==0:
                    new.remove(ch)
                break
            else:
                k-=tot
                cnt[ind]+=1
        if st==n:
            break
        char=[]+new
    return ''.join(ans)

'''Line Segment Intersection'''
def orientation(point1,point2,point3):
    ori=(point2[1]-point1[1])*(point3[0]-point1[0])-(point3[1]-point1[1])*(point2[0]-point1[0])
    if ori==0:
        return 0    #on the line
    elif ori>0:
        return 1    #right
    else:
        return -1   #left
    
def do_intersect(point1,point2,point3,point4):
    o1=orientation(point1,point2,point3)
    o2=orientation(point1,point2,point4)
    o3=orientation(point3,point4,point1)
    o4=orientation(point3,point4,point2)
    on_segment=lambda point1,point2,point3:min(point1[0],point2[0])<=point3[0]<=max(point1[0],point2[0]) and min(point1[1],point2[1])<=point3[1]<=max(point1[1],point2[1])
    if o1!=o2 and o3!=o4:
        return True
    if o1==0 and on_segment(point1,point2,point3):
        return True
    if o2==0 and on_segment(point1,point2,point4):
        return True
    if o3==0 and on_segment(point3,point4,point1):
        return True
    if o4==0 and on_segment(point3,point4,point2):
        return True
    return False

'''Matrix exponentiation'''
#[[F(n)]+[F(n-1)]]=(Transformation matrix**k)*(matrix for base cases)

def multiply_matrices(mat1,mat2):
    n=len(mat1)
    res=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][k]+=mat1[i][j]*mat2[j][k]
    return res

#You just have to make the mat matrix by yourself
def exp(n,p):
    ans=[[1,0],[0,1]]
    mat=[[1-p,p],[p,1-p]]
    while n:
        if n%2:
            ans=multiply_matrices(ans,mat)
        mat=multiply_matrices(mat,mat)
        n>>=1
    return ans[0][0]

'''Mobius Function'''
def sieve(n):
    global prime,mu
    prime=[1]*(n+1)
    prime[0]=0
    prime[1]=0
    mu=[-1]*(n+1)
    for i in range(2,n+1):
        if prime[i]:
            mu[i]*=-1
            num=i+i
            while num<=n:
                if not num%(i*i):
                    mu[num]=0
                elif mu[num]:
                    mu[num]*=-1
                prime[num]=0
                num+=i

#Use when n>mod and mod is a composite number
#prime factorisation of mod=p1*p2*p3*...*pn
#pass these pi in this function one by one

def nCr_modp(n,r,mod,fact):
    res=1
    while n or r:
        m,j=n%mod,r%mod
        if j>m:
            return 0
        num=fact[m]
        den=(fact[j]*fact[m-j])%mod
        invden=1
        for x in range(1,mod):
            if (den*x)%mod==1:
                invden=x
                break
        cur=(num*invden)%mod
        res=(res*cur)%mod
        n//=mod
        r//=mod
    return res

def nCr_mod1_mul_mod2(n,r,mod1,mod2):
    a=nCr_modp(n,r,mod1)
    b=nCr_modp(n,r,mod2)
    if mod1<mod2:
        mod1,mod2=mod2,mod1
        a,b=b,a
    ans=0
    for i in range(mod2):
        if (ans+a)%mod2==b:
            return ans+a
        ans+=mod1
    return 0

'''
NTT
x1+x2+x3+....+xk=n where xi>=thr, then number of solutions ((1,2) and (2,1) is different) is
coefficient of t**n in (t**thr + t**(thr+1) + .... + t**n)**k

Pass this as [0,0,1(thr index),1,1,....,1(nth index)]**k

If you want the summation of n!/(x1! * x2! * .... * xk!),
find the coefficient of ((t**thr)/thr! + (t**(thr+1))/(thr+1)! + .... (t**n)/n!) and multiply it by n!
'''

mod=998244353
primitive_root=3

def NTT(a,invert=False):
    n=len(a)
    j=0
    for i in range(1,n):
        bit=n>>1
        while j&bit:
            j^=bit
            bit>>=1
        j^=bit
        if i<j:
            a[i],a[j]=a[j],a[i]

    length=2
    while length<=n:
        wlen=pow(primitive_root,(mod-1)//length,mod)
        if invert:
            wlen=pow(wlen,-1,mod)
        for i in range(0,n,length):
            w=1
            for j in range(length//2):
                u=a[i+j]
                v=a[i+j+length//2]*w%mod
                a[i+j]=(u+v)%mod
                a[i+j+length//2]=(u-v+mod)%mod
                w=w*wlen%mod
        length<<=1

    if invert:
        inv_n=pow(n,-1,mod)
        for i in range(n):
            a[i]=a[i]*inv_n%mod

def multiply_polynomials(poly1,poly2):
    n=1
    while n<len(poly1)+len(poly2):
        n<<=1
    a=poly1+[0]*(n-len(poly1))
    b=poly2+[0]*(n-len(poly2))

    NTT(a,invert=False)
    NTT(b,invert=False)
    
    for i in range(n):
        a[i]=a[i]*b[i]%mod
        
    NTT(a,invert=True)
    
    return a         #Always truncate it to the required powers


'''Polynomial Rolling Hash'''
#Use this when you dont know the pattern which you are looking for in a string.
#If you know the pattern, use z_function or kmp, as it runs faster
class Rolling_hash:

    def __init__(self,n):
        from random import randint
        self.prime=[29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599]
        self.base1=self.prime[randint(0,99)]
        self.mod1=10**9+7
        self.power1=[1]
        cur1=1
        self.base2=self.prime[randint(0,99)]
        self.mod2=10**9+9
        self.power2=[1]
        cur2=1
        for i in range(n):
            cur1,cur2=(cur1*self.base1)%self.mod1,(cur2*self.base2)%self.mod2
            self.power1.append(cur1)
            self.power2.append(cur2)

    #Returns two dictionaries with keys=hash value and values=start index
    def get_hash(self,string,window_size):
        hash_vals1={}
        hash_vals2={}
        cur1,cur2=0,0
        start_index=0
        for i,j in enumerate(string):
            if i<window_size-1:
                cur1=(cur1*self.base1+ord(j)-ord('a')+1)%self.mod1
                cur2=(cur2*self.base2+ord(j)-ord('a')+1)%self.mod2
            else:
                cur1=(cur1*self.base1+ord(j)-ord('a')+1)%self.mod1
                if hash_vals1.get(cur1,[]):
                    hash_vals1[cur1].append(start_index)
                else:
                    hash_vals1[cur1]=[start_index]
                cur1=(cur1-self.power1[window_size-1]*(ord(string[start_index])-ord('a')+1))%self.mod1
                cur2=(cur2*self.base2+ord(j)-ord('a')+1)%self.mod2
                if hash_vals2.get(cur2,[]):
                    hash_vals2[cur2].append(start_index)
                else:
                    hash_vals2[cur2]=[start_index]
                cur2=(cur2-self.power2[window_size-1]*(ord(string[start_index])-ord('a')+1))%self.mod2
                start_index+=1
        return hash_vals1,hash_vals2

    def count(self,string,pattern):
        window_size=len(pattern)
        hs1,hs2=self.get_hash(string,window_size)
        hp1,hp2=self.get_hash(pattern,window_size)
        hash_of_pattern=list(hp1.keys())[0]
        cnt1=0
        last=-1
        for ind in hs1.get(hash_of_pattern):
            if last<ind:
                last=ind+window_size-1
                cnt1+=1
        hash_of_pattern=list(hp2.keys())[0]
        cnt2=0
        last=-1
        for ind in hs2.get(hash_of_pattern):
            if last<ind:
                last=ind+window_size-1
                cnt2+=1
        return min(cnt1,cnt2)


'''Reroot Template'''
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

'''Segment Tree'''
class SegmentTree:
    
    def __init__(self,l,merge,default):
        self.merge=merge
        self.default=default
        self.n=1<<len(l).bit_length() if len(l)&(len(l)-1) else len(l)
        self.seg=[self.default for i in range(2*self.n)]
        for i in range(self.n,2*self.n):
            if i-self.n>=len(l):
                break
            else:
                self.seg[i]=l[i-self.n]
        for ind in range(self.n-1,0,-1):
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1 based indexing
    def update(self,ind,val):
        ind=ind+self.n-1
        self.seg[ind]=val
        while ind>1:
            ind>>=1
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1 based indexing
    def query(self,left,right):                  
        left,right=left+self.n-1,right+self.n-1

        resL,resR=self.default,self.default    #Default value
            
        while left<=right:
            if left&1:
                resL=self.merge(resL,self.seg[left])
                left+=1
            if not right&1:
                resR=self.merge(self.seg[right],resR)
                right-=1
            left>>=1
            right>>=1
        return self.merge(resL,resR)

    def __repr__(self):
        return f'SegmentTree([{', '.join(map(str,[self.query(i,i) for i in range(1,self.n+1)]))}])'

class LazySegmentTree:

    def __init__(self,l,merge,default):
        self.merge=merge
        self.default=default
        self.n=1<<len(l).bit_length() if len(l)&(len(l)-1) else len(l)
        self.seg=[self.default for i in range(2*self.n)]
        self.lazy=[0]*(2*self.n)
        for i in range(self.n,2*self.n):
            if i-self.n>=len(l):
                break
            else:
                self.seg[i]=l[i-self.n]
        for ind in range(self.n-1,0,-1):
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1-based indexing (val is val to be added not assigned)
    def update(self,left,right,val):
        
        if left>right:
            return
        
        stk=[]
        ind,low,high=1,1,self.n
        stk.append((ind,low,high))
        tra=[]
        
        while stk:
            
            ind,low,high=stk.pop()
            
            self.pull(ind,low,high)
                
            if left<=low<=high<=right:
                self.push(ind,low,high,val)
                    
            elif low<=left<=high or low<=right<=high:
                mid=(low+high)//2
                stk.append((2*ind+1,mid+1,high))
                stk.append((2*ind,low,mid))
                tra.append((ind,low,high))
                
        while tra:
            ind,low,high=tra.pop()
            self.seg[ind]=self.merge(self.seg[2*ind],self.seg[2*ind+1])

    #Pass 1-based indexing
    def query(self,left,right):
        
        if left>right:
            return self.default
        
        stk=[]
        ind,low,high=1,1,self.n
        stk.append((ind,low,high))
        ans=self.default
        
        while stk:
            
            ind,low,high=stk.pop()

            self.pull(ind,low,high)
                
            if left<=low<=high<=right:
                ans=self.merge(ans,self.seg[ind])
                
            elif low<=left<=high or low<=right<=high:
                mid=(low+high)//2
                stk.append((2*ind+1,mid+1,high))
                stk.append((2*ind,low,mid))
                
        return ans

    def pull(self,ind,low,high):
        if self.lazy[ind]!=0:
            lazy_val=self.lazy[ind]
            self.seg[ind]+=(high-low+1)*lazy_val   #Change as needed
            if ind<self.n:
                self.lazy[2*ind]+=lazy_val
                self.lazy[2*ind+1]+=lazy_val
            self.lazy[ind]=0

    def push(self,ind,low,high,val):
        self.seg[ind]+=(high-low+1)*val       #Change as needed
        if ind<self.n:
            self.lazy[2*ind]+=val
            self.lazy[2*ind+1]+=val

    def __repr__(self):
        return f'SegmentTree([{', '.join(map(str,[self.query(i,i) for i in range(1,self.n+1)]))}])'


'''Square Root Decomposition'''
class SquareRootDecomposition:

    def __init__(self,l,merge,default):
        self.n=len(l)
        self.size=int(pow(self.n,0.5))   #Size of each block
        self.l=l
        self.merge=merge
        self.default=default
        self.blocks=[]
        for i,j in enumerate(l):
            if i%self.size:
                cur=self.merge(cur,j)
            else:
                cur=self.default
                cur=self.merge(cur,j)
            if i%self.size==self.size-1 or i==self.n-1:
                self.blocks.append(cur)

    #Pass 1-based indexing
    def update(self,ind,val):
        ind-=1
        self.l[ind]=val
        start=ind-(ind%self.size)
        end=min(start+self.size,self.n)
        cur=self.default
        for i in range(start,end):
            cur=self.merge(cur,self.l[i])
        self.blocks[ind//self.size]=cur

    #Pass 1-based indexing
    def query(self,left,right):
        left,right=left-1,right-1
        start=left//self.size
        end=right//self.size
        if start==end:
            cur=self.default
            for i in range(left,right+1):
                cur=self.merge(cur,self.l[i])
        else:
            cur=self.default
            #Left half
            if not left%self.size:
                cur=self.merge(cur,self.blocks[start])
            else:
                while left%self.size:
                    cur=self.merge(cur,self.l[left])
                    left+=1
            #Mid
            for i in range(start+1,end):
                cur=self.merge(cur,self.blocks[i])
            #Right half
            if right%self.size==self.size-1:
                cur=self.merge(cur,self.blocks[end])
            else:
                while right%self.size!=self.size-1:
                    cur=self.merge(cur,self.l[right])
                    right-=1
        return cur

class Mos_Algo:

    def __init__(self,l):
        self.n=len(l)
        self.size=int(pow(self.n,0.5))   #Size of each block (Play with it for good runtime)
        self.l=l

    def add(self,ele):
        old=self.cnt.get(ele,0)
        if old:
            self.item.discard((-old,ele))
        new=old+1
        self.cnt[ele]=new
        self.item.add((-new,ele))

    def remove(self,ele):
        old=self.cnt.get(ele,0)
        self.item.discard((-old,ele))
        new=old-1
        self.cnt[ele]=new
        if new:
            self.item.add((-new,ele))

    def answer(self,thr):
        freq,ele=self.item[0]
        return ele if -freq>=thr else -1

    #Always pass queries with idx as the index of the query inserted at the last
    #Pass 1-based indexing for left and right
    #Time complexity is O(N*no_of_blocks + Q*block_size)*O(add,remove,answer)
    def query(self,queries):
        queries.sort(key=lambda x:(x[0]//self.size,-x[1]) if (x[0]//self.size)%2 else (x[0]//self.size,x[1]))
        res=[-1]*len(queries)
        curl,curr=0,-1
        self.cnt={}
        self.item=SortedList()
        for left,right,idx in queries:  #Take care here
            left,right=left-1,right-1  #For 0-based indexing
            while curr<right:
                curr+=1
                self.add(self.l[curr])
            while curr>right:
                self.remove(self.l[curr])
                curr-=1
            while curl<left:
                self.remove(self.l[curl])
                curl+=1
            while curl>left:
                curl-=1
                self.add(self.l[curl])
            res[idx]=self.answer(thr)
        return res


'''String Algorithms'''
def manacher(t):
    ##Length of longest palindrome having centre at index i (in p it is 2*i+1) is p[i]-1
    s=['#']+list('#'.join(t))+['#']
    n=len(s)
    p=[1]*n
    l,r=1,1
    for i in range(1,n):
        p[i]=max(0,min(r-i,p[l+r-i]))
        while 0<=i-p[i] and i+p[i]<n and s[i-p[i]]==s[i+p[i]]:
            p[i]+=1
        if i+p[i]>r:
            l,r=i-p[i],i+p[i]
    return p

#Pass 1-based indexing for l and r
def checkPal(l,r,p):
    l-=1
    r-=1
    lp,rp=2*l+1,2*r+1
    return p[(lp+rp)//2]>=r-l+2


def z_func(s):
    ##z_list[i]=Maximum length l of prefix[0,i-1] which is also a substring[i,n-1]
    n=len(s)
    z_list=[0]*n
    left=0
    right=0
    for i in range(1,n):
        if i<right:
            z_list[i]=min(z_list[i-left],right-i)
        while i+z_list[i]<n and s[z_list[i]]==s[i+z_list[i]]:
            z_list[i]+=1
        if i+z_list[i]>right:
            left=i
            right=i+z_list[i]
    return z_list
 
def kmp(s):
    #pre[i]=Maximum length l of prefix[0,i-1] which is also a suffix[1,i]
    n=len(s)
    pre=[0]*n
    for i,j in enumerate(pre):
        if i==0:
            continue
        ma=pre[i-1]
        while(ma>0 and s[i]!=s[ma]):
            ma=pre[ma-1]
        if s[i]==s[ma]:
            ma+=1
        pre[i]=ma
    return pre
 
'''Tarzan's Algorithm (Bridges in Graph)'''
vis=[0]*(v+1)
min_step=[0]*(v+1)
step=[0]*(v+1)
bridge=[]

@bootstrap              
def Tarzan(tin,parent,grand_par=0):
    vis[parent]=True
    lowest_time[parent]=tin
    for child in adj[parent]:
        if child==grand_par:
            continue
        if not vis[child]:
            yield Tarzan(tin+1,child,parent)
            if tin<lowest_time[child]:
                bridge.append((parent,child))
        lowest_time[parent]=min(lowest_time[parent],lowest_time[child])
    yield

'''Trie DS'''
#For binary strings
class TrieNode:
    
    def __init__(self):
        self.left=None
        self.right=None
        self.cnt=0
        self.isEnd=0

class Trie:
    
    def __init__(self,bits):
        self.root=TrieNode()
        #ai<2**30 Here,30 is number of bits, j.bit_length()
        self.bits=bits
        self.power=[1]
        for i in range(self.bits-1):
            self.power.append(self.power[-1]*2)

    def insert(self,number):
        cur=self.root
        for bit in range(self.bits-1,-1,-1):
            if self.power[bit]&number:
                if not cur.right:
                    cur.right=TrieNode()
                cur=cur.right
            else:
                if not cur.left:
                    cur.left=TrieNode()
                cur=cur.left
            cur.cnt+=1
        cur.isEnd+=1

    def remove(self,number):
        cur=self.root
        for bit in range(self.bits-1,-1,-1):
            if self.power[bit]&number:
                cur=cur.right
            else:
                cur=cur.left
            cur.cnt-=1
        cur.isEnd-=1

    def search(self,number):
        cur=self.root
        for bit in range(self.bits-1,-1,-1):
            if self.power[bit]&number:
                cur=cur.right
            else:
                cur=cur.left
            if not (cur and cur.cnt):
                return False
        return True if cur.isEnd else False

    def max_xor(self,number):
        cur=self.root
        ans=0
        for bit in range(self.bits-1,-1,-1):
            if self.power[bit]&number:
                if cur.left and cur.left.cnt:
                    cur=cur.left
                    ans|=self.power[bit]
                else:
                    cur=cur.right
            else:
                if cur.right and cur.right.cnt:
                    cur=cur.right
                    ans|=self.power[bit]
                else:
                    cur=cur.left
        return ans

#For strings consisting of alphabets
class TrieNode:
    
    def __init__(self):
        self.cnt=0
        self.node=[None]*26
        self.isEnd=0

class Trie:
    
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            if not cur.node[ind]:
                cur.node[ind]=TrieNode()
            cur=cur.node[ind]
            cur.cnt+=1
        cur.isEnd+=1

    def remove(self,word):
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            cur.node[ind].cnt-=1
            cur=cur.node[ind]
        cur.isEnd-=1

    def search(self,word):
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            if not (cur.node[ind] and cur.node[ind].cnt):
                return False
            cur=cur.node[ind]
        return True if cur.isEnd else False

'''Xor Basis'''
def create_basis(arr):
    basis=[]
    for j in arr:
        for base in basis:
            j=min(j,j^base)
        if j:
            basis.append(j)
    basis.sort()
    return basis

def clean_basis(basis):
    n=len(basis)
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            basis[j]=min(basis[j],basis[j]^basis[i])
    return basis

#The smallest xor is 0 which is of empty subset
def kth_smallest_xor_subset(basis,k):
    ans=0
    bit=0
    while k:
        if k&1:
            ans+=basis[bit]
        k>>=1
        bit+=1
    return ans
