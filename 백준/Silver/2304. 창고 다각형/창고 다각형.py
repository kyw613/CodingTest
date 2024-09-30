N = int(input())

graph = []
for _ in range(N):
    x,y = map(int,input().split())
    graph.append([x,y])

graph.sort(key=lambda x:(-x[1]))#높은거 기준으로
#이제 여기서 right_min이랑 left_max비교
S = graph[0][1]
r_start = graph[0][0] + 1
r_end = max([x[0] for x in graph]) + 1  
l_start = min([x[0] for x in graph])
l_end = graph[0][0]

for i in range(1,len(graph)):
    if graph[i][0] >=r_start:
        S += (graph[i][0]+1-r_start) * graph[i][1]
        r_start = graph[i][0] + 1
    elif graph[i][0] <= l_end:
        S += (l_end-graph[i][0]) * graph[i][1]
        l_end = graph[i][0]

print(S)




