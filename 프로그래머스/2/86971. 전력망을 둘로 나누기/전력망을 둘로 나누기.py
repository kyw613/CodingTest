from collections import defaultdict, deque

def bfs(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return count

def solution(n, wires):
    # 그래프 생성
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    min_difference = float('inf')  # 차이의 최소값을 무한대로 초기화

    # 모든 전선을 하나씩 끊어봄
    for v1, v2 in wires:
        # 전선 끊기
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # 두 서브트리의 크기 계산
        count1 = bfs(graph, v1, n)  # v1을 시작으로 한 서브트리 크기
        count2 = n - count1  # 전체 송전탑에서 count1을 뺀 나머지 서브트리 크기

        # 최소 차이 계산
        min_difference = min(min_difference, abs(count1 - count2))

        # 전선 복구
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_difference
