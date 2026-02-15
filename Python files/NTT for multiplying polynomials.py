'''
x1+x2+x3+....+xk=n where xi>=thr, then number of solutions ((1,2) and (2,1) is different) is
coefficient of t**n in (t**thr + t**(thr+1) + .... + t**n)**k

Pass this as [0,0,1(thr index),1,1,....,1(nth index)]**k

If you want the summation of n!/(x1! * x2! * .... * xk!),
find the coefficient of ((t**thr)/thr! + (t**(thr+1))/(thr+1)! + .... (t**n)/n!) and multiply it by n!
'''

mod=998244353
primitive_root=3

def NTT(a,invert=False):
    n=len(a)
    j=0
    for i in range(1,n):
        bit=n>>1
        while j&bit:
            j^=bit
            bit>>=1
        j^=bit
        if i<j:
            a[i],a[j]=a[j],a[i]

    length=2
    while length<=n:
        wlen=pow(primitive_root,(mod-1)//length,mod)
        if invert:
            wlen=pow(wlen,-1,mod)
        for i in range(0,n,length):
            w=1
            for j in range(length//2):
                u=a[i+j]
                v=a[i+j+length//2]*w%mod
                a[i+j]=(u+v)%mod
                a[i+j+length//2]=(u-v+mod)%mod
                w=w*wlen%mod
        length<<=1

    if invert:
        inv_n=pow(n,-1,mod)
        for i in range(n):
            a[i]=a[i]*inv_n%mod

def multiply_polynomials(poly1,poly2):
    n=1
    while n<len(poly1)+len(poly2):
        n<<=1
    a=poly1+[0]*(n-len(poly1))
    b=poly2+[0]*(n-len(poly2))

    NTT(a,invert=False)
    NTT(b,invert=False)
    
    for i in range(n):
        a[i]=a[i]*b[i]%mod
        
    NTT(a,invert=True)
    
    return a         #Always truncate it to the required powers

