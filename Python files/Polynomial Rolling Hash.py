#from math import *
#from collections import *
#from bisect import *
#from heapq import *
#from random import *

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *args,sep=' ',end='\n':stdout.write(sep.join(map(str,args))+end)

def out(l):
    print(' '.join(map(str,l)))

def yes():
    print('Yes')

def no():
    print('No')

def alice():
    print('Alice')

def bob():
    print('Bob')

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

def solve():
    s=input()
    p=input()
    obj=Rolling_hash(len(s))
    print(obj.count(s,p))
        
for _ in range(1):
    solve()
