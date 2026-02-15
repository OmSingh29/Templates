def optimized_knapsack(arr,max_sum,left=-1,right=-1,bits=16384):
    '''
    Returns a dp array where dp[i]<(2**bits)-1
    Each bit of each element denotes whether the subset sum of 'position of bit' is possible or not
    Time complexity is max_sum*len(tot)/bits
    if left and right is given:
        Returns True if any of the sum between [left,right] is possible else False
    else:
        Returns dp array
    
    Example:
    dp=[3,5,9],bits=4
    bit of dp element->  1 0 1 1    0 1 0 1    1 0 0  1        (1 if summation is possible else 0)
    position of bit->    0 1 2 3    4 5 6 7    8 9 10 11
    Takes 3 secs to execute when n*n=4*10**10
    '''
    m=(max_sum+1)//bits
    dp=[0]*(m+1)
    dp[0]=power[bits-1]
    if not left==right==-1:
        start_block,end_block=left//bits,right//bits
        reqs,reqe=bits-(left%bits),bits-(right%bits+1)
    for j in arr:
        j=bits*(m+1)-1-j
        block=j//bits
        req=bits-(j%bits+1)
        for i in range(m,-1,-1):
            cur=((dp[block-1]&(power[req]-1))*power[bits-req] if block else 0)|(dp[block]//power[req])
            dp[i]|=cur

            if left==right==-1:
                pass
            elif start_block==end_block:
                if i==start_block and (dp[i]&(power[reqs]-1))//power[reqe]:
                    return True
            elif (start_block<i<end_block and dp[i]) or (i==start_block and dp[i]&(power[reqs]-1)) or (i==end_block and dp[i]//power[req]):
                return True
            
            if not block:
                break
            block-=1
    return dp if left==right==-1 else False

bits=16384
power=[1]
for i in range(bits):
    power.append(power[-1]<<1)
