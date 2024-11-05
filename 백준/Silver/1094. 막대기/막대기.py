import heapq

X = int(input())
q = []
heapq.heappush(q, 64)
total = 64

while total > X:
    l = heapq.heappop(q)
    half = l // 2
    heapq.heappush(q, half)
    if total - half >= X:
        total -= half
    else:
        heapq.heappush(q, half)

print(len(q))
