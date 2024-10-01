from collections import deque

# 입력 받기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 출발점 찾기
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            start, end = x, y
            graph[x][y] = 0  # 출발점은 0으로 설정

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    # 거리 배열 초기화 (-1로 초기화)
    distance = [[-1] * m for _ in range(n)]
    distance[x][y] = 0  # 출발점은 거리가 0
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이미 방문했거나 벽인 경우 무시
            if graph[nx][ny] == 0 or distance[nx][ny] != -1:
                continue

            # 처음 방문하는 경우 거리 갱신 및 큐에 추가
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

    # 도달할 수 없는 0은 그대로 유지
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and distance[i][j] == -1:
                distance[i][j] = 0

    return distance

# 출발점에서 BFS 실행
result = bfs(start, end)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
