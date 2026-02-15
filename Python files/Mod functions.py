#Mod functions

def nCr(n,r,mod=None):
    if n<r or r<0:
        return 0
    r=min(r,n-r)
    num,den=1,1
    for i in range(1,r+1):
        num*=n-i+1
        den*=i
        if mod:
            num%=mod
            den%=mod
    return (num*pow(den,-1,mod))%mod if mod else num//den

def nPr(n,r):
    if n<r or r<0:
        return 0
    ans=1
    for i in range(n-r+1,n+1):
        ans*=i
    return ans

def factorial(n):
    global fact,inv
    fact=[1]
    for i in range(1,n+1):
        fact.append((fact[-1]*i)%mod)
    inv=[1]*(n+1)
    inv[n]=pow(fact[-1],-1,mod)
    for i in range(n-1,0,-1):
        inv[i]=(inv[i+1]*(i+1))%mod

def nPr(n,r):
    return fact[n]*inv[n-r]%mod if r>=0 and n>=r else 0

def nCr(n,r):
    return (fact[n]*(inv[r]*inv[n-r]%mod))%mod if r>=0 and n>=r else 0

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

