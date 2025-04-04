from collections import deque
M,N,K = map(int,input().split())
graph = [[0]* N for _ in range(M)] 
for _ in range(K):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            graph[j][i] = 1
visit = [[True]* N for _ in range(M)] 
result = []
def bfs(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    q = deque([(y,x)])
    visit[y][x] = False
    cnt = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y + dy[i],x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if graph[ny][nx] == 0 and visit[ny][nx] == True:
                    visit[ny][nx] = False
                    cnt += 1
                    q.append((ny,nx))
    return cnt

for i in range(M):
    for j in range(N):
        if visit[i][j] == True and graph[i][j] == 0:
            val = bfs(i,j)
            result.append(val)

print(len(result))
print(" ".join(map(str,sorted(result))))