import heapq
N = int(input())
q = []
for tc in range(N):
    a = int(input())
    if a >= 0:
        ty = 1
    else:
        ty = -1
    if a == 0:
        if q:
            val,t = heapq.heappop(q)
            print(t*val)
        else:
            print("0")
    else:
        heapq.heappush(q,(abs(a),ty))

