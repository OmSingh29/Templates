#[[F(n)]+[F(n-1)]]=(Transformation matrix**k)*(matrix for base cases)

def multiply_matrices(mat1,mat2):
    n=len(mat1)
    res=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][k]+=mat1[i][j]*mat2[j][k]
    return res

#You just have to make the mat matrix by yourself
def exp(n,p):
    ans=[[1,0],[0,1]]
    mat=[[1-p,p],[p,1-p]]
    while n:
        if n%2:
            ans=multiply_matrices(ans,mat)
        mat=multiply_matrices(mat,mat)
        n>>=1
    return ans[0][0]
