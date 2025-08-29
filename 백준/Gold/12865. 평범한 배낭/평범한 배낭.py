N,K = map(int,input().split())
arr = [(0,0)]
for i in range(N):
    w,v = map(int,input().split())
    arr.append((w,v))

DP = [[0]*(K+1) for _ in range(N+1)] # 0-idx
#print(DP)

for i in range(1, N + 1):#개수
    weight, value = arr[i]
    for j in range(1, K + 1):# 배낭 용량
        if weight <= j:
            DP[i][j] = max(DP[i-1][j-weight] + value, DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][K])
