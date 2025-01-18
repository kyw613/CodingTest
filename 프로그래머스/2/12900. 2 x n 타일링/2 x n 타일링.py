def solution(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    prev2 = 1  # dp[0]
    prev1 = 1  # dp[1]

    for _ in range(2, n + 1):
        curr = (prev1 + prev2) % 1000000007
        prev2 = prev1
        prev1 = curr

    return prev1
