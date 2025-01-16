def solution(land):
    row = len(land)
    col = len(land[0])
    dp = [[0] * col for _ in range(row)]
    for i in range(4):
        dp[0][i] = land[0][i]
    for k in range(1,row):
        # 아래가 아니면 가장 큰것을 
        for t in range(4):
            if t == 0:
                dp[k][t] = int(land[k][t]) + int(max(dp[k-1][1:]))
            elif t == 3:
                dp[k][t] = int(land[k][t]) + int(max(dp[k-1][:t]))
            else:
                dp[k][t] = int(land[k][t]) + int(max(max(dp[k-1][:t]),max(dp[k-1][t+1:])))
    return (max(dp[-1]))