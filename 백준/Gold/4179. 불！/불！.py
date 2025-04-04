from collections import deque

def bfs(start, fire_list):
    f_stack = fire_list[:]
    s_stack = deque([(1, start[0], start[1])])
    while s_stack:
        f = []
        s = []
        for f_y, f_x in f_stack:
            for i in range(4):
                f_ny = f_y + dy[i]
                f_nx = f_x + dx[i]
                if 0 <= f_ny < N and 0 <= f_nx < M:
                    if arr[f_ny][f_nx] == ".":
                        f.append((f_ny, f_nx))
                        arr[f_ny][f_nx] = "F"
        for idx, s_y, s_x in s_stack:
            for i in range(4):
                ny = s_y + dy[i]
                nx = s_x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if arr[ny][nx] == "." and visit[ny][nx]:
                        visit[ny][nx] = False
                        if ny == 0 or ny == N-1 or nx == 0 or nx == M-1:
                            return idx + 1
                        s.append((idx + 1, ny, nx))
        f_stack = f[:]
        s_stack = s[:]
    return -1

N, M = map(int, input().split())
arr = []
fire_list = []

for i in range(N):
    a = input()
    row = list(a)
    for j in range(len(row)):
        if row[j] == "J":
            start = (i, j)
            row[j] = "."
        elif row[j] == "F":
            fire_list.append((i, j))
    arr.append(row)

# 시작 위치가 가장자리면 즉시 탈출
if start[0] == 0 or start[0] == N-1 or start[1] == 0 or start[1] == M-1:
    print(1)
    exit()

visit = [[True] * M for _ in range(N)]
visit[start[0]][start[1]] = False

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

res = bfs(start, fire_list)
if res == -1:
    print("IMPOSSIBLE")
else:
    print(res)
