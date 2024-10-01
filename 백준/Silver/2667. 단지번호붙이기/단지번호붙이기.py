from collections import deque

N = int(input())

graph = []
for _ in range(N):
    # 입력을 한 줄로 받아 각 문자들을 개별 정수로 변환하여 리스트로 저장
    graph.append(list(map(int, input().strip())))

result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x_start, y_start):
    cnt = 1
    queue = deque()
    queue.append((x_start, y_start))
    visited[x_start][y_start] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    
    return cnt

# BFS 탐색을 통해 단지의 크기를 찾음
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1 and not visited[x][y]:
            result.append(bfs(x, y))

# 결과를 오름차순으로 정렬 후 출력
result.sort()
print(len(result))  # 단지의 수 출력
for i in result:
    print(i)
