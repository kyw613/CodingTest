import heapq
import sys
input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    a = int(input())
    if a == 0:
        if not heap:
            print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,a)
        