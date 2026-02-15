from collections import deque

from sys import stdin,stdout
input=lambda:stdin.readline().rstrip()
print=lambda *x,sep=' ',end='\n':stdout.write(sep.join(map(str,x))+end)

def out(l):
    print(' '.join(map(str,l)))

def yes():
    print('Yes')

def no():
    print('No')
        
def valid(x,y):
    return 0<=x<=n-1 and 0<=y<=m-1

def bfs():
    while q:
        a,b=q.pop()
        for i,j in move:
            if valid(a+i,b+j) and lvl[a+i][b+j]>lvl[a][b]+l[a+i][b+j]:
                if l[a+i][b+j]==0:
                    q.append((a+i,b+j))
                else:
                    q.appendleft((a+i,b+j))
                lvl[a+i][b+j]=lvl[a][b]+l[a+i][b+j]

def solve():
    global v,e,v_a,adj_list,tra,hght,dpth,par_list,lvl,q,move,n,m,l
    n,m=map(int,input().split())
    move=[[0,1],[1,0],[0,-1],[-1,0]]
    q=deque()
    l=[]
    for i in range(n):
        l1=list(map(int,list(input())))
        l.append(l1)
    _ind=[]
    lvl=[[float('inf')]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 or j==0 or i==n-1 or j==m-1:
                if l[i][j]==0:
                    lvl[i][j]=0
                    q.append((i,j))
                else:
                    lvl[i][j]=1
                    q.appendleft((i,j))
            if l[i][j]==0:
                _ind.append([i,j])
    bfs()
    ma=0
    for i,j in _ind:
        ma=max(ma,lvl[i][j])
    print(ma)

for _ in range(int(input())):
    solve()
