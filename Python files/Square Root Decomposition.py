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
