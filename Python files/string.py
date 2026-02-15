def func(s):
    n=len(s)
    last=[-1]*26
    mini=float('inf')
    for i,j in enumerate(s):
        idx=ord(j)-ord('a')
        if last[idx]!=-1:
            mini=min(mini,i-last[idx])
        last[idx]=i
    return n-mini
    
print(func('anxab'))
