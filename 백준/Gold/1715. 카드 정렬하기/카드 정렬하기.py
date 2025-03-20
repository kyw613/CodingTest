import heapq
N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q,int(input()))
cnt = 0
while len(q) != 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    c = a+b
    heapq.heappush(q,c)
    cnt += c
print(cnt)
