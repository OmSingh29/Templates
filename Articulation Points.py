#from math import ceil,log
#from collections import deque,Counter
#from bisect import bisect
#from heapq import heappush,heappop
#from random import randint

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

@bootstrap
def articulation_point(cnt,par,grand_par=0):
    vis[par]=1
    min_step[par]=cnt
    tin[par]=cnt
    ch=0
    for child in adj[par]:
        if child==grand_par:
            continue
        if not vis[child]:
            yield articulation_point(cnt+1,child,par)
            min_step[par]=min(min_step[par],min_step[child])
            if grand_par and min_step[child]>=tin[par]:
                art[par]=1
            ch+=1
        else:
            min_step[par]=min(min_step[par],tin[child])
    if not grand_par and ch>1:
        art[par]=1
    yield

def solve():
    global adj,vis,tin,min_step,art
    v,e=map(int,input().split())
    vis=[0]*(v+1)
    art=[0]*(v+1)
    min_step=[0]*(v+1)
    tin=[0]*(v+1)
    adj=[[] for i in range(v+1)]
    for i in range(e):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
    articulation_point(1,1)
    print(art)
        
for _ in range(int(input())):
    solve()
