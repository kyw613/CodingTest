from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    exit()

MAX_SIZE = max(2 * K, 100000)
DP = [1000001] * (MAX_SIZE + 1)
DP[N] = 0
order = deque([N])


while order:
    val = order.popleft()
    # *2 이동
    if val * 2 <= MAX_SIZE and DP[val * 2] > DP[val]:
        DP[val * 2] = DP[val]
        order.appendleft(val * 2)

    # +1 이동 
    if val + 1 <= MAX_SIZE and DP[val + 1] > DP[val] + 1:
        DP[val + 1] = DP[val] + 1
        order.append(val + 1)

    # -1 이동
    if val - 1 >= 0 and DP[val - 1] > DP[val] + 1:
        DP[val - 1] = DP[val] + 1
        order.append(val - 1)

print(DP[K])
