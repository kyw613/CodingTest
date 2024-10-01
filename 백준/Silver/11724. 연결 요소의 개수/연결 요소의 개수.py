from collections import deque
N, M = map(int,input().split()) #정점의 개수 N과 간선의 개수 M
graph = [[] for _ in range(N+1)]  #방향없는 그래프

for i in range(M):  
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [False for _ in range(N+1)]
# bfs로 visited한후에 한번에 끝나냐 아니냐로 하면 되네
def bfs(start,graph,visited):
    queue = deque()
    queue.append((start))
    while queue:
        x = queue.popleft()
        if not visited[x]: # 안왔다면 True로 바꾸고 지난것들도 넣는다 
            visited[x] = True
            for i in graph[x]:
                queue.append(i)
        
    return 1
result = 0
for x in range(1,N+1):
    if not visited[x]:
        bfs(x, graph, visited)
        result += 1

print(result)