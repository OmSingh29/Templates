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
        
def solve():
    global vis,adj,lowest_time,bridge
    #v=int(input())
    v,e=map(int,input().split())
    vis=[0]*(v+1)
    min_step=[0]*(v+1)
    step=[0]*(v+1)
    bridge=[]
    ans=v*(v-1)//2
    adj=[[] for i in range(v)]
    for i in range(e):
        x,y=map(int,input().split())
        adj[x-1].append(y)
        adj[y-1].append(x)
    Tarzan(1,1)
    print(bridge)
    

for _ in range(int(input())):
    solve()

