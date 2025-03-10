#from math import *
from collections import *
#from bisect import *
#from heapq import *

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)

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

def vis(a):
    #v_a=visited array defined globally and a is the number with smallest value 1
    if v_a[a-1]==1:
        return True
    else:
        return False

@bootstrap              
def Tarzan(tin,par,grand_par=0):
    #a is the root node for traversal (a>0)
    v_a[par-1]=1
    min_step[par]=tin
    #tra.append(a)
    for i,child in enumerate(adj_list[par-1]):
        if child==grand_par:
            continue
        if not vis(child):
            yield Tarzan(tin+1,child,par)
            min_step[par]=min(min_step[child],min_step[par])
            if min_step[child]>tin:
                bridge.append((par,child))
        else:
            min_step[par]=min(min_step[child],min_step[par])
    yield

def iter_Tarzan(root):
    tra=[]
    stk=[]
    stk.append((root,0))
    cnt=1
    while stk:
        par,grand_par=stk.pop()
        v_a[par-1]=1
        min_step[par]=cnt
        step[par]=cnt
        cnt+=1
        tra.append((par,grand_par))
        for i,child in enumerate(adj_list[par-1]):
            if child==grand_par:
                continue
            if not vis(child):
                stk.append((child,par))
            else:
                min_step[par]=min(min_step[child],min_step[par])

    for ind,ch_par in enumerate(tra[::-1]):
        child=ch_par[0]
        par=ch_par[1]
        if par==0:
            continue
        min_step[par]=min(step[child],step[par])
        if min_step[child]>step[par]:
            bridge.append((par,child))
        
def solve():
    global v,e,v_a,adj_list,min_step,bridge,step
    #v=int(input())
    v,e=map(int,input().split())
    v_a=[0]*v
    min_step=[0]*(v+1)
    step=[0]*(v+1)
    bridge=[]
    ans=v*(v-1)//2
    adj_list=[[] for i in range(v)]
    for i in range(e):
        x,y=map(int,input().split())
        adj_list[x-1].append(y)
        adj_list[y-1].append(x)
    Tarzan(1,1)
    print(bridge)
    

for _ in range(int(input())):
    solve()

