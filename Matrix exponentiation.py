def mul(mat1,mat2):
    n=len(mat1)
    res=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][k]+=mat1[i][j]*mat2[j][k]
    return res

def exp(n,p):
    ans=[[1,0],[0,1]]
    mat=[[1-p,p],[p,1-p]]
    while n:
        if n%2:
            ans=mul(ans,mat)
        mat=mul(mat,mat)
        n//=2
    return ans[0][0]
