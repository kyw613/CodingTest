from collections import deque
N = int(input())
array = []
for _ in range(N):
    array.append(input())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
arrayed = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if array[y][x] =="G":
            arrayed[y][x] = "R"
        else:
            arrayed[y][x] = array[y][x]

visited = [[True] * N for _ in range(N)]
visit = [[True] * N for _ in range(N)]
def rg_bfs(N,visited,array,y,x):
    q = deque([(y,x)])
    if visited[y][x] == False:
        return False
    visited[y][x] = False
    comp = array[y][x]
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y + dy[i],x+dx[i]
            if 0<=ny< N and 0 <= nx < N and visited[ny][nx] == True and array[ny][nx] == comp:
                q.append((ny,nx))
                visited[ny][nx] = False
    return True

cnt_nrg = 0
cnt = 0
for y in range(N):
    for x in range(N):
        if rg_bfs(N,visit,array,y,x):
            cnt_nrg += 1
        if rg_bfs(N,visited,arrayed,y,x):
            cnt += 1


print(cnt_nrg,cnt)