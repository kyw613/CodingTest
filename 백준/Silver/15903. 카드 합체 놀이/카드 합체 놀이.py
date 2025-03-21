import heapq
N,M = map(int,input().split())
q = []
arr = list(map(int,input().split()))
for a in arr:
    heapq.heappush(q,a)
for _ in range(M):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q,a+b)
    heapq.heappush(q,a+b)
print(sum(q))
