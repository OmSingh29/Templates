#Time Complexity: O(26*n) => O(n)
#Returns empty string if k>valid permutations
def lexicographically_kth_string(s,k):
    def nCr(n,r,limit):
        if n<r or r<0:
            return 0
        r=min(r,n-r)
        ans=1
        for i in range(1,r+1):
            ans*=n-i+1
            ans//=i
            if ans>limit:
                return limit+1
        return ans

    def permutation(st):
        tot=1
        pos=n-st
        for i,j in enumerate(cnt):
            if not j:
                continue
            tot*=nCr(pos,j,k)
            if tot>k:
                return tot
            pos-=j
        return tot

    n=len(s)
    cnt=[0]*26
    for j in s:
        cnt[ord(j)-ord('a')]+=1
    char=[]
    for i,j in enumerate(cnt):
        if j:
            char.append(chr(ord('a')+i))
    st=0
    tot=permutation(0)
    if tot<k:
        return ''
    ans=[]
    while True:
        new=[]+char
        for ch in char:
            ind=ord(ch)-ord('a')
            cnt[ind]-=1
            tot=permutation(st+1)
            if tot>=k:
                ans.append(ch)
                st+=1
                if cnt[ind]==0:
                    new.remove(ch)
                break
            else:
                k-=tot
                cnt[ind]+=1
        if st==n:
            break
        char=[]+new
    return ''.join(ans)

print(lexicographically_kth_string('abcd',24))
