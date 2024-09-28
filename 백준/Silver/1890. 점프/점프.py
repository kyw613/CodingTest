N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

directions = [(1, 0), (0, -1)]  # 오른쪽 아래 순서!

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1 

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and graph[i][j] > 0:
            if j + graph[i][j] < N: #x축
                dp[i][j + graph[i][j]] += dp[i][j]
            if i + graph[i][j] < N: #y축
                dp[i + graph[i][j]][j] += dp[i][j]

print(dp[N-1][N-1])