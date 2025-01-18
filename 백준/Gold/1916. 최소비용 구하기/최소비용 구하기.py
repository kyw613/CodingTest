import heapq
import sys

N = int(input())  # 도시 개수
M = int(input())  # 버스 개수

# 버스 정보를 저장할 리스트
bus = [[] for _ in range(N + 1)]

# 버스 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))  # (도착 도시, 비용)

start, end = map(int, input().split())

# 다익스트라 알고리즘 초기화
pos = [1000000000] * (N + 1)
pos[start] = 0

q = []
heapq.heappush(q, (0, start))  # (현재 비용, 현재 노드)

while q:
    cost, current = heapq.heappop(q)

    if cost > pos[current]:
        continue

    for destination, val in bus[current]:
        new_cost = cost + val
        if new_cost < pos[destination]:
            pos[destination] = new_cost
            heapq.heappush(q, (new_cost, destination))

print(pos[end])
