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

#For strings of alphabets
class TrieNode:
    
    def __init__(self):
        self.a=None
        self.b=None
        self.c=None
        self.d=None
        self.e=None
        self.f=None
        self.g=None
        self.h=None
        self.i=None
        self.j=None
        self.k=None
        self.l=None
        self.m=None
        self.n=None
        self.o=None
        self.p=None
        self.q=None
        self.r=None
        self.s=None
        self.t=None
        self.u=None
        self.v=None
        self.w=None
        self.x=None
        self.y=None
        self.z=None
        self.cnt=0
        self.isEnd=0

class Trie:
    
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            if ind==0:
                if not cur.a:
                    cur.a=TrieNode()
                cur=cur.a
            elif ind==1:
                if not cur.b:
                    cur.b=TrieNode()
                cur=cur.b
            elif ind==2:
                if not cur.c:
                    cur.c=TrieNode()
                cur=cur.c
            elif ind==3:
                if not cur.d:
                    cur.d=TrieNode()
                cur=cur.d
            elif ind==4:
                if not cur.e:
                    cur.e=TrieNode()
                cur=cur.e
            elif ind==5:
                if not cur.f:
                    cur.f=TrieNode()
                cur=cur.f
            elif ind==6:
                if not cur.g:
                    cur.g=TrieNode()
                cur=cur.g
            elif ind==7:
                if not cur.h:
                    cur.h=TrieNode()
                cur=cur.h
            elif ind==8:
                if not cur.i:
                    cur.i=TrieNode()
                cur=cur.i
            elif ind==9:
                if not cur.j:
                    cur.j=TrieNode()
                cur=cur.j
            elif ind==10:
                if not cur.k:
                    cur.k=TrieNode()
                cur=cur.k
            elif ind==11:
                if not cur.l:
                    cur.l=TrieNode()
                cur=cur.l
            elif ind==12:
                if not cur.m:
                    cur.m=TrieNode()
                cur=cur.m
            elif ind==13:
                if not cur.n:
                    cur.n=TrieNode()
                cur=cur.n
            elif ind==14:
                if not cur.o:
                    cur.o=TrieNode()
                cur=cur.o
            elif ind==15:
                if not cur.p:
                    cur.p=TrieNode()
                cur=cur.p
            elif ind==16:
                if not cur.q:
                    cur.q=TrieNode()
                cur=cur.q
            elif ind==17:
                if not cur.r:
                    cur.r=TrieNode()
                cur=cur.r
            elif ind==18:
                if not cur.s:
                    cur.s=TrieNode()
                cur=cur.s
            elif ind==19:
                if not cur.t:
                    cur.t=TrieNode()
                cur=cur.t
            elif ind==20:
                if not cur.u:
                    cur.u=TrieNode()
                cur=cur.u
            elif ind==21:
                if not cur.v:
                    cur.v=TrieNode()
                cur=cur.v
            elif ind==22:
                if not cur.w:
                    cur.w=TrieNode()
                cur=cur.w
            elif ind==23:
                if not cur.x:
                    cur.x=TrieNode()
                cur=cur.x
            elif ind==24:
                if not cur.y:
                    cur.y=TrieNode()
                cur=cur.y
            else:
                if not cur.z:
                    cur.z=TrieNode()
                cur=cur.z
            cur.cnt+=1
        cur.isEnd+=1

    def remove(self,word):
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            if ind==0:
                cur=cur.a
            elif ind==1:
                cur=cur.b
            elif ind==2:
                cur=cur.c
            elif ind==3:
                cur=cur.d
            elif ind==4:
                cur=cur.e
            elif ind==5:
                cur=cur.f
            elif ind==6:
                cur=cur.g
            elif ind==7:
                cur=cur.h
            elif ind==8:
                cur=cur.i
            elif ind==9:
                cur=cur.j
            elif ind==10:
                cur=cur.k
            elif ind==11:
                cur=cur.l
            elif ind==12:
                cur=cur.m
            elif ind==13:
                cur=cur.n
            elif ind==14:
                cur=cur.o
            elif ind==15:
                cur=cur.p
            elif ind==16:
                cur=cur.q
            elif ind==17:
                cur=cur.r
            elif ind==18:
                cur=cur.s
            elif ind==19:
                cur=cur.t
            elif ind==20:
                cur=cur.u
            elif ind==21:
                cur=cur.v
            elif ind==22:
                cur=cur.w
            elif ind==23:
                cur=cur.x
            elif ind==24:
                cur=cur.y
            else:
                cur=cur.z
            cur.cnt-=1
        cur.isEnd-=1

    def search(self,word):
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            if ind==0:
                cur=cur.a
            elif ind==1:
                cur=cur.b
            elif ind==2:
                cur=cur.c
            elif ind==3:
                cur=cur.d
            elif ind==4:
                cur=cur.e
            elif ind==5:
                cur=cur.f
            elif ind==6:
                cur=cur.g
            elif ind==7:
                cur=cur.h
            elif ind==8:
                cur=cur.i
            elif ind==9:
                cur=cur.j
            elif ind==10:
                cur=cur.k
            elif ind==11:
                cur=cur.l
            elif ind==12:
                cur=cur.m
            elif ind==13:
                cur=cur.n
            elif ind==14:
                cur=cur.o
            elif ind==15:
                cur=cur.p
            elif ind==16:
                cur=cur.q
            elif ind==17:
                cur=cur.r
            elif ind==18:
                cur=cur.s
            elif ind==19:
                cur=cur.t
            elif ind==20:
                cur=cur.u
            elif ind==21:
                cur=cur.v
            elif ind==22:
                cur=cur.w
            elif ind==23:
                cur=cur.x
            elif ind==24:
                cur=cur.y
            else:
                cur=cur.z
            if not (cur and cur.cnt):
                return False
        return True if cur.isEnd else False
