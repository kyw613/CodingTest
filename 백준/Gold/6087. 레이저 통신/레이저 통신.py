from collections import deque

W, H = map(int, input().split())
grid = [input().rstrip() for _ in range(H)]

C = []
for y in range(H):
    for x in range(W):
        if grid[y][x] == 'C':
            C.append((y, x))
(sy, sx), (ey, ex) = C[0], C[1]

INF = 10**9
dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]

dy = [-1, 0, 1, 0]
dx = [ 0, 1, 0,-1]

dq = deque()

# 처음엔 거울사용않고 어디든 가능 + 다익스트라 + bfs느낌
for d in range(4):
    dist[sy][sx][d] = 0
    dq.append((sy, sx, d))

while dq:
    y, x, d = dq.popleft()
    if dist[y][x][d] > min(dist[y][x]):
        continue

    # 네 방향으로 시도
    for nd in range(4):
        ny, nx = y + dy[nd], x + dx[nd]
        if not (0 <= ny < H and 0 <= nx < W): 
            continue
        if grid[ny][nx] == '*':
            continue

        add = 0 if d == nd else 1  # 같은 방향 0, 회전 1
        # 시작점에서 첫 발은 거울로 치지 않도록, sy,sx에서 바로 나가는 것도 위 규칙으로 처리 가능
        cost = dist[y][x][d] + add
        if dist[ny][nx][nd] > cost:
            dist[ny][nx][nd] = cost
            # 비용 0이면 앞에, 1이면 뒤에
            if add == 0:
                dq.appendleft((ny, nx, nd))
            else:
                dq.append((ny, nx, nd))

print(min(dist[ey][ex]))
