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
