from collections import deque
N,K = map(int,input().split())
arr = [0]* 200001 # 0부터 100000까지
visit = [True] * 200001


def bfs(now,K):
    step = [(1,1),(1,-1),(2,0)]
    q = deque([(0,now)])
    visit[now] = False
    while q:
        idx,now = q.popleft()
        if now == K:
            return idx
        for i in range(3):
            next = step[i][0] * now+ step[i][1]
            if 0 <= next <= 200000 and visit[next] == True:
                visit[next] = False
                q.append((idx+1,next))

print(bfs(N,K))

        