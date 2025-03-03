from collections import deque
N, K = map(int,input().split())
number = []
for _ in range(N):
    number.append(int(input()))

dp = [K+1]*(K+1)
dp[0] = 0
q = deque()
q.append(0)
while q:
    val = q.popleft()
    for n in number:
        if val + n <= K and dp[val] + 1 < dp[val+n]:
            dp[val+n] = dp[val] + 1
            q.append(val+n)
if dp[K] == K+1:
    print("-1")
else:   
    print(dp[K])