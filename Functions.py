def divisors(n):
    if n==1:
        return [1]
    div=[1,n]
    i=2
    while i*i<=n:
        if not n%i:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
        i+=1
    return div

def prime_factors(n):
    if n==1:
        return []
    num=n
    facs=[]
    i=2
    while i*i<=n:
        if not num%i:
            facs.append(i)
        while not num%i:
            num//=i
        if num==1:
            break
        i+=1
    else:
        facs.append(num)
    return facs

def sieve(n):
    global prime
    prime=[1]*(n+1)
    '''
    global lp,hp
    lp=[1]*(n+1)
    lp[0]=0
    hp=[1]*(n+1)
    hp[0]=0
    '''
    prime[0]=0
    prime[1]=0
    for i in range(2,n+1):
        if prime[i]:
            num=i+i
            '''
            hp[i]=i
            if lp[i]==1:
                lp[i]=i
            '''
            while num<=n:
                '''
                hp[num]=i
                if lp[num]==1:
                    lp[num]=i
                '''
                prime[num]=0
                num+=i
                
# Returns all the prime numbers between [n:n+1000+1]
# n+i is a prime number if prime[i]==1
# Time Complexity sqrt(n+1000)log(n+1000)
# log(10**12)=39.86
# largest prime gap for n<=10**15 is 924
def range_sieve(n):
    global prime
    prime=[1]*(1001)
    prime[0]=0 if n==1 else 1
    y=ceil(pow(n+1000,0.5))
    for i in range(2,y+1):
        num=2*i if i>=n else ((n+i-1)/i)*i
        while num<=n+1000:
            prime[num-n]=0
            num+=i

sieve(10**5)
l=[]
cnt=0
for i,j in enumerate(prime):
    if j:
        l.append(i)
        cnt+=1
    if cnt==10:
        break
print(l)
