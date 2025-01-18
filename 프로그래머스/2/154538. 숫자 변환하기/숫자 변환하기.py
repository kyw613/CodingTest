def solution(x, y, n):
    # DP문제인듯 
    # x를 y로 변환이니까
    # heapq쓰면 편할듯? 만들고 안되면 써보자
    dp = [0] * (y+1) # 1-idx
    dp[x] = 1
    for k in range(x,y):
        if dp[k] != 0:
            if k+n <= y:
                if dp[k+n] != 0:
                    dp[k+n] = min(dp[k+n], dp[k]+1)
                else:
                    dp[k+n] = dp[k] + 1
            if 2*k <= y:
                if dp[2*k] != 0:
                    dp[2*k] = min(dp[2*k],dp[k] + 1)
                else:
                    dp[2*k] = dp[k] + 1
            if 3*k <= y:
                if dp[3*k] != 0:
                    dp[3*k] = min(dp[3*k],dp[k] + 1)
                else:
                    dp[3*k] = dp[k] + 1
    if dp[-1] == 0:
        return -1
    else:
        return dp[-1]-1
            