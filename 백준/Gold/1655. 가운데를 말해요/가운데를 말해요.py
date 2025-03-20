import sys
import heapq

input = sys.stdin.readline
N = int(input())

left_q = []  # 최대 힙
right_q = []  # 최소 힙

for _ in range(N):
    num = int(input())

    # 1. left_q에 먼저 삽입 (최대 힙 유지)
    heapq.heappush(left_q, -num)
    # 2. left_q의 최대값이 right_q의 최소값보다 크다면 조정
    if right_q and -left_q[0] > right_q[0]:
        max_val = -heapq.heappop(left_q)
        min_val = heapq.heappop(right_q)

        heapq.heappush(left_q, -min_val)
        heapq.heappush(right_q, max_val)

    # 3. 크기 균형 유지 (left_q는 항상 right_q보다 같거나 하나 많아야 함)
    if len(left_q) > len(right_q) + 1:
        heapq.heappush(right_q, -heapq.heappop(left_q))

    print(-left_q[0])
