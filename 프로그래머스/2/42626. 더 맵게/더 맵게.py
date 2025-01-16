import heapq
def solution(scoville, K):
    # 가장 낮은 2개의 음식을  가장 안매운거 + (2번째로 안매운거) * 2
    # heapq 
    q = []
    for i in scoville:
        heapq.heappush(q,i)
    cnt = 0
    while True:
        comp = q[0]
        if q[0] < K:
            if len(q) <= 1:
                return -1
            cnt += 1
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            heapq.heappush(q,first+2*second)
        else:
            break
    return cnt
        
        