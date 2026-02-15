#Gives the indices of strictly smaller or greater elements
def previous_element(l):
    stks,pse=[],[]
    stkg,pge=[],[]
    for i,j in enumerate(l):
        #For smaller elements
        while stks and j<=l[stks[-1]]:
            stks.pop()
        if stks:
            pse.append(stks[-1])
        else:
            pse.append(-1)
        stks.append(i)
        #For larger elements
        while stkg and l[stkg[-1]]<=j:
            stkg.pop()
        if stkg:
            pge.append(stkg[-1])
        else:
            pge.append(-1)
        stkg.append(i)
    return pse,pge

def next_element(l):
    n=len(l)
    stks,nse=[],[n]*n
    stkg,nge=[],[n]*n
    for i in range(n-1,-1,-1):
        j=l[i]
        #For smaller elements
        while stks and j<=l[stks[-1]]:
            stks.pop()
        if stks:
            nse[i]=stks[-1]
        stks.append(i)
        #For greater elements
        while stkg and l[stkg[-1]]<=j:
            stkg.pop()
        if stkg:
            nge[i]=stkg[-1]
        stkg.append(i)
    return nse,nge
