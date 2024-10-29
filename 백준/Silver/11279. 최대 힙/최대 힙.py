import heapq
import sys
input = sys.stdin.readline
N = int(input())
q = []

for i in range(N):
    input_data = int(input())
    if input_data == 0:
        if not q:
            print("0")
        else:
            val = heapq.heappop(q)
            print(-val)
    else:
        heapq.heappush(q,-input_data)
