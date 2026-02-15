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
        return f"SegmentTree([{', '.join(map(str,[self.query(i,i) for i in range(1,self.n+1)]))}])"

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
            
def solve():
    n=int(input())
    l=list(map(int,input().split()))
    obj=SegmentTree(l,max,0)
    q=int(input())
    for i in range(q):
        li=list(map(int,input().split()))
        if li[0]==1:
            op,idx,val=li
            obj.update(idx,val)
        else:
            op,left,right=li
            print(obj.query(left,right))
        print(obj)
        
for _ in range(int(input())):
    solve()

'''
1
10
0 0 0 0 0 0 0 0 0 0
50
'''
