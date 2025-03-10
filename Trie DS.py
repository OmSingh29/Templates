#from math import *
#from collections import *
#from bisect import *
#from heapq import *
#from random import *

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)


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
        

def solve():
    obj=Trie()
    q=int(input())
    for i in range(q):
        x,y=input().split()
        if x=='+':
            obj.insert(y)
        elif x=='-':
            obj.remove(y)
        else:
            print(obj.search(y))
        
for _ in range(int(input())):
    solve()
