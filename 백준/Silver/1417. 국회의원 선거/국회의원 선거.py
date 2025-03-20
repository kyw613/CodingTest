import heapq
N = int(input())
q = []
vote_me = int(input())
if N <= 1:
    print("0")
else:

    for _ in range(N-1):
        a = int(input())
        heapq.heappush(q,-a)

    cnt = 0
    while True:
        val = heapq.heappop(q)
        if -val < vote_me:
            break
        else:
            val += 1
            vote_me += 1
            heapq.heappush(q,val)
            cnt += 1
    print(cnt)