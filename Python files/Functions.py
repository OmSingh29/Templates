'''
Goldbach's conjecture, a famous unsolved problem in number theory, posits that
every even integer greater than 2 can be expressed as the sum of two prime numbers.
'''

def sieve(n):
    global isprime
    isprime=[True]*(n+1)
    isprime[0],isprime[1]=False,False
    sq=int(pow(n,0.5))
    for i in range(2,sq+1):
        if not isprime[i]:
            continue
        for j in range(i*i,n+1,i):
            isprime[j]=False

#For lowest prime factor,use this as it is more fast
def sieve(n):
    global isprime,lp
    isprime,lp=[True]*(n+1),[1]*(n+1)
    isprime[0],isprime[1]=False,False
    lp[0],lp[1]=0,0
    for i in range(2,n+1):
        if not isprime[i]:
            continue
        if lp[i]==1:
            lp[i]=i
        for j in range(i*i,n+1,i):
            if lp[j]==1:
                lp[j]=i
            isprime[j]=False

def sieve(n):
    global isprime,lp,hp
    isprime,lp,hp=[True]*(n+1),[1]*(n+1),[1]*(n+1)
    isprime[0],isprime[1]=False,False
    lp[0],hp[0]=0,0
    for i in range(2,n+1):
        if not isprime[i]:
            continue
        hp[i]=i
        if lp[i]==1:
            lp[i]=i
        for j in range(2*i,n+1,i):
            hp[j]=i
            if lp[j]==1:
                lp[j]=i
            isprime[j]=False

#Returns all prime numbers in the range [start>=1,end]
def range_sieve(start,end):
    #Calculate primes till sqrt(n)
    global mark,isprime,primes
    n=int(pow(end,0.5))
    mark,primes=[True]*(n+1),[]
    mark[0]=mark[1]=False
    for i in range(2,n+1):
        if not mark[i]:
            continue
        primes.append(i)
        for j in range(i*i,n+1,i):
            mark[j]=False
    #Using marked primes to get primes in [start,end]
    isprime=[True]*(end-start+1)
    if start==1:
        isprime[0]=False
    for i in primes:
        num=(start-1)-((start-1)%i)
        for j in range(max(i*i,num+i),end+1,i):
            isprime[j-start]=False

def divisors(n):
    '''
    Returns sorted list of divisors of n in O(sqrt(n))
    '''
    if n==1:
        return [1]
    small_divs=[1]
    large_divs=[n]
    i=2
    while i*i<=n:
        if not n%i:
            small_divs.append(i)
            if i!=n//i:
                large_divs.append(n//i)
        i+=1
    return small_divs+large_divs[::-1]

def prime_factorisation(n):
    '''
    Returns a list of tuples where l[i]=(prime,cnt) in O(sqrt(n))
    '''
    num=n
    prime_facs=[]
    i=2
    while i*i<=n:
        cnt=0
        while not num%i:
            num//=i
            cnt+=1
        if cnt:
            prime_facs.append((i,cnt))
        if num==1:
            break
        i+=1
    if num!=1:
        prime_facs.append((num,1))
    return prime_facs

def prime_factorisation(n):
    '''
    Returns a list of tuples where l[i]=(prime,cnt) in O(log(n))
    '''
    num=n
    prime_facs=[]
    num=n
    while num>1:
        last=lp[num]
        cnt=0
        while lp[num]==last:
            num//=last
            cnt+=1
        prime_facs.append((last,cnt))
    return prime_facs

def divisors(n):
    '''
    Returns list of divisors (not sorted) of n in O(no. of divs)
    '''
    if n==1:
        return [1]
    prime_facs=prime_factorisation(n)
    divs=[1]
    for prime,cnt in prime_facs:
        tot=len(divs)
        for i in range(tot-1,-1,-1):
            div=divs[i]
            for j in range(cnt):
                div*=prime
                divs.append(div)
    return divs

def calculate_sum(n):
    '''
    Returns sum of digits from 1 to n in O(log(n))
    '''
    nn=n
    ans=0
    coeff=1
    while nn:
        j=nn%10
        quo=n//(coeff*10)
        rem=n%coeff
        ans+=45*coeff*quo
        ans+=j*(j-1)//2*coeff
        ans+=j*(rem+1)
        coeff*=10
        nn//=10
    return ans

def isprime(num):
    if num<=1:
        return False
    i=2
    while i*i<=num:
        if not num%i:
            return False
        i+=1
    return True

def fraction(num,den):
    if den==0:
        return (1,0)
    elif num==0:
        return (0,1)
    else:
        g=gcd(abs(num),abs(den))
        num,den=num//g,den//g
        if den<0:
            num,den=-num,-den
        return (num,den)

# Miller-Rabin primality test O((log(n))**3)
def is_prime(n,k=5):  # number of tests
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0:
        return False
 
    # write n-1 as 2^r * d
    r,d =0,n-1
    while d%2==0:
        d//=2
        r+=1
 
    # witness loop
    from random import randrange
    for _ in range(k):
        a=randrange(2,n-1)
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        for _ in range(r-1):
            x=pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True

def divide(dividend,divisor):
    quo=[]
    rem=0
    for j in dividend:
        j=int(j)
        rem*=10
        rem+=j
        if quo or rem//divisor:
            quo.append(str(rem//divisor))
        rem%=divisor
    if not quo:
        quo.append('0')
    return ''.join(quo),rem

