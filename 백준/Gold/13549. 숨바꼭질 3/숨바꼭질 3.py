N,K = map(int,input().split())
from collections import deque
# 1. DP 사용하기
if N >= K:
    print(N-K)
    exit()
max_size = max(2*K, 100000)
DP = [1000001]* (max_size+1)
DP[N] = 0
order = deque([N])
while order:
    val = order.popleft()
    if val * 2 <=max_size:
        a = DP[2*val]
        DP[2*val] = min(DP[2*val],DP[val])
        if a != DP[2*val]:
            order.append(2*val)
    if val + 1 <= max_size:
        b = DP[val+1]
        DP[val+1] = min(DP[val+1],DP[val]+1)
        if b != DP[val+1]:
            order.append(val+1)
    if val - 1 >= 0:
        c = DP[val-1]
        DP[val-1] = min(DP[val-1],DP[val]+1)
        if c != DP[val-1]:
            order.append(val-1)
print(DP[K])