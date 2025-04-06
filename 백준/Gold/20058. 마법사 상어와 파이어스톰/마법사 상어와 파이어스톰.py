from collections import deque

# 입력 처리
N, Q = map(int, input().split())
size = 2 ** N
arr = [list(map(int, input().split())) for _ in range(size)]
L_list = list(map(int, input().split()))

# 시계 방향 90도 회전 (부분 배열 회전)
def rotate(arr, l):
    n = len(arr)
    res = [[0] * n for _ in range(n)]
    block = 2 ** l
    for y in range(0, n, block):
        for x in range(0, n, block):
            for i in range(block):
                for j in range(block):
                    res[y + j][x + block - 1 - i] = arr[y + i][x + j]
    return res

# 얼음 감소
def melt(arr):
    n = len(arr)
    new_arr = [row[:] for row in arr]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(n):
        for x in range(n):
            if arr[y][x] == 0:
                continue
            cnt = 0
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > 0:
                    cnt += 1
            if cnt < 3:
                new_arr[y][x] -= 1
    return new_arr

# BFS로 덩어리 크기 측정
def bfs(y, x, arr, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    cnt = 1
    n = len(arr)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and arr[ny][nx] > 0:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt

# 파이어스톰 시전
for l in L_list:
    arr = rotate(arr, l)
    arr = melt(arr)

# 얼음 총합
total = sum(map(sum, arr))

# 가장 큰 얼음 덩어리
visited = [[False]*size for _ in range(size)]
max_block = 0
for y in range(size):
    for x in range(size):
        if not visited[y][x] and arr[y][x] > 0:
            max_block = max(max_block, bfs(y, x, arr, visited))

# 출력
print(total)
print(max_block)
