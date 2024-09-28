N, D = map(int, input().split())
shortcuts = []

for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:  # 도착 위치가 고속도로 범위 안에 있을때만
        shortcuts.append((s,e,d))

dp = [10001] * (D + 1)
dp[0] = 0  # 시작점은 0

# 0부터 D까지 최소 거리
for i in range(D + 1):
    # (1칸 이동)
    if i + 1 <= D:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    
    # 지름길을 이용
    for s,e,d in shortcuts:
        if i == s and e <= D:
            dp[e] = min(dp[e], dp[i] + d)

print(dp[D])
