import heapq
N = int(input())
heap = []
for _ in range(N):
    day,val = map(int,input().split())
    heapq.heappush(heap,(-val,day))

dp = [0] * (1001) # 이거 0은 빼야함
# 큰거부타 나오게 ㄱㄱ
while heap:
    val,day = heapq.heappop(heap)
    for i in range(day,-1,-1):
        if dp[i] == 0:
            dp[i] = -val
            break
print(sum(dp)-dp[0])

