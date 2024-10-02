N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, 1, 0]
dy = [0, 1, 1]

score = [[0 for _ in range(M)] for _ in range(N)]
score[0][0] = graph[0][0]  # 시작점

# 위에서부터 시작하여 3방향으로만 움직인다.
for y in range(N):
    for x in range(M):
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                score[ny][nx] = max(score[ny][nx], score[y][x] + graph[ny][nx])

print(score[N-1][M-1])
