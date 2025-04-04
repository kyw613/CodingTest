from collections import deque
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
#arr의 min,max구하기
max_val = max(map(max, arr))
min_val = min(map(min, arr))
def bfs(y,x,size):
    dy,dx = [-1,1,0,0],[0,0,-1,1]
    q = deque([(y,x)])
    visit[y][x] = False
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visit[ny][nx] == True and arr[ny][nx] >size:
                    q.append((ny,nx))
                    visit[ny][nx] = False
    return 1

max_cnt = 1
for k in range(min_val-1,max_val+1):
    cnt = 0
    visit = [[True]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and visit[i][j] == True:
                cnt += bfs(i,j,k)
    max_cnt = max(max_cnt,cnt)
print(max_cnt)


