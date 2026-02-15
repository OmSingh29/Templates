def intersectIntervals(intervals1,intervals2):
    intervals1.sort()
    intervals2.sort()
    answer=[]
    i,j=0,0
    while i<len(intervals1) and j<len(intervals2):
        start=max(intervals1[i][0],intervals2[j][0])
        end=min(intervals1[i][1],intervals2[j][1])
        if start<=end:
            answer.append((start,end))
        if intervals1[i][1]<intervals2[j][1]:
            i+=1
        else:
            j+=1
    return answer
