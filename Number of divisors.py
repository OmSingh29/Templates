n=int(input("Enter the n:"))
fac=[0]*(n+1)
for i in range(1,n+1):
    for j in range(i,n+1,i):
        fac[j]+=1
ma=max(fac)
print('Maximum number of factors is',ma,'of the number',fac.index(ma))
