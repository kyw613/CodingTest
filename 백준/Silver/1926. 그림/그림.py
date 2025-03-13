from collections import deque

def bfs(y,x,array,visit):
    q = deque([(y,x)])
    visit[y][x] = False
    cnt = 1
    ty = False
    while q:
        ty = True
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == True and array[ny][nx]==1:
                visit[ny][nx] = False
                cnt += 1
                q.append((ny,nx))
    return [cnt,ty]


N,M = map(int,input().split())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]

picture_cnt = 0
max_cnt = 0
a = 0
visit = [[True] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if visit[y][x] and array[y][x] ==1:
            a,ty= bfs(y,x,array,visit)
            if ty:
                max_cnt = max(a,max_cnt)
                picture_cnt += 1
print(picture_cnt)
print(max_cnt)

        







