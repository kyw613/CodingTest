from sys import stdin
from collections import deque

input = stdin.readline

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j


def bfs(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    tmp = []
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        tmp.append((nx, ny, distance[nx][ny]))

    # 거리 , x, y좌표 순으로 정렬하여 거리가 동일한 경우 가장 왼쪽 위에 있는 좌표가 삭제될 수 있도록 만듬
    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
res = 0
while 1:
    shark = bfs(x, y, size)
    # 길이가 0이면 탐색 종료
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    # 시간 더해주기
    res += dist
    graph[x][y], graph[nx][ny] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮겨준다.
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(res)