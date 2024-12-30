def solution(n):
    # 최대 개수잖아
    # dp로 갈수있는 칸 계속 하기?
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567