def sieve(n):
    global prime,mu
    prime=[1]*(n+1)
    prime[0]=0
    prime[1]=0
    mu=[-1]*(n+1)
    for i in range(2,n+1):
        if prime[i]:
            mu[i]*=-1
            num=i+i
            while num<=n:
                if not num%(i*i):
                    mu[num]=0
                elif mu[num]:
                    mu[num]*=-1
                prime[num]=0
                num+=i
sieve(30)
print(mu)
'''
n=30
mobi=[1]*(n+1)
mobi[1]=0
for i in range(2,n+1):
    for j in range(2*i,n+1,i):
        mobi[j]-=mobi[i]
print(mobi)
'''
