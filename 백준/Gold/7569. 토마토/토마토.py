from collections import deque
M,N,H = map(int,input().split()) # 가로 세로 높이
graph = [[[0]*M for _ in range(N)] for _ in range(H)] # 이걸 걍 3차원으로 만들어..
start = deque()
for h in range(H):
    for y in range(N):
        li = list(map(int,input().split()))
        for x in range(len(li)):
            if li[x] != 0:
                graph[h][y][x] = li[x]
                if li[x] == 1:
                    start.append((0,h,y,x))
visit = [[[True] * M for _ in range(N)] for _ in range(H)]


dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]



while start:
    idx,h,y,x = start.popleft()
    visit[h][y][x] = False
    for i in range(6):
        nh,ny,nx = h+dh[i],y+dy[i],x+dx[i]
        if 0<=nh<H and 0<= ny < N and 0 <= nx < M and visit[nh][ny][nx]==True and graph[nh][ny][nx] == 0:
            visit[nh][ny][nx] = False
            graph[nh][ny][nx] = 1
            start.append((idx+1,nh,ny,nx))
for h in range(H):
    ty = False
    for y in range(N):
        for x in range(M):
            if graph[h][y][x] == 0:
                ty = True
                print("-1")
                break
        if ty:
            break
    if ty:
        break
if not ty:
    print(idx)

