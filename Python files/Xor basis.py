def create_basis(arr):
    basis=[]
    for j in arr:
        for base in basis:
            j=min(j,j^base)
        if j:
            basis.append(j)
    basis.sort()
    return basis

def clean_basis(basis):
    n=len(basis)
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            basis[j]=min(basis[j],basis[j]^basis[i])
    return basis

#The smallest xor is 0 which is of empty subset
def kth_smallest_xor_subset(basis,k):
    ans=0
    bit=0
    while k:
        if k&1:
            ans+=basis[bit]
        k>>=1
        bit+=1
    return ans
