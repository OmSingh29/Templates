#Mod functions

mod=1000000007

def add(x,y):
    return ((x%mod)+(y%mod))%mod

def sub(x,y):
    return (x-y+mod)%mod

def mul(x,y):
    return ((x%mod)*(y%mod))%mod

def mod_inv(x):
    return pow(x,-1,mod)

def factorial(n):
    global fact,inv
    fact=[1]
    for i in range(1,n+1):
        fact.append(mul(fact[-1],i))
    inv=[1]*(n+1)
    inv[n]=mod_inv(fact[-1])
    for i in range(n-1,0,-1):
        inv[i]=mul(inv[i+1],i+1)

def nPr(n,r):
    return mul(fact[n],inv[n-r]) if r>=0 and n>=r else 0

def nCr(n,r):
    return mul(fact[n],mul(inv[r],inv[n-r])) if r>=0 and n>=r else 0

#If you have to take mod2, then it also works:
#Checks if r is a factor of n or not
def nCr_mod2(n,r):
    return n&r==r

#Use when n>mod and mod is a composite number
#prime factorisation of mod=p1*p2*p3*...*pn
#pass these pi in this function one by one

def factorial(mod):
    fact=[1]
    for i in range(1,mod):
        fact.append((fact[-1]*i)%mod)
    return fact

def nCr_modp(n,r,mod,fact):
    res=1
    while n or r:
        m,j=n%mod,r%mod
        if j>m:
            return 0
        num=fact[m]
        den=(fact[j]*fact[m-j])%mod
        invden=1
        for x in range(1,mod):
            if (den*x)%mod==1:
                invden=x
                break
        cur=(num*invden)%mod
        res=(res*cur)%mod
        n//=mod
        r//=mod
    return res

def nCr_mod1_mul_mod2(n,r,mod1,mod2):
    a=nCr_modp(n,r,mod1)
    b=nCr_modp(n,r,mod2)
    if mod1<mod2:
        mod1,mod2=mod2,mod1
        a,b=b,a
    ans=0
    for i in range(mod2):
        if (ans+a)%mod2==b:
            return ans+a
        ans+=mod1
    return 0

factorial(80)
#print(fact)

