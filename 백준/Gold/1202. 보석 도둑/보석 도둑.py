import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []  # 보석 리스트 (무게, 가치)
for _ in range(N):
    m, v = map(int, input().split())
    A.append((m, v))

A.sort()  # 보석을 무게 기준 오름차순 정렬

B = []  # 가방 리스트
for _ in range(K):
    B.append(int(input()))
B.sort()  # 가방을 무게 기준 오름차순 정렬

result = 0
possible_jewels = []  # 가방에 넣을 수 있는 보석들 (가치 기준 최대 힙)
jewel_index = 0

for b in B:
    # 현재 가방의 무게 제한 b보다 작은 보석들을 모두 우선순위 큐에 넣음
    while jewel_index < N and A[jewel_index][0] <= b:
        heapq.heappush(possible_jewels, -A[jewel_index][1])  # 가치는 최대 힙을 위해 음수로 저장
        jewel_index += 1

    # 넣을 수 있는 보석 중 가장 가치가 큰 것을 꺼냄
    if possible_jewels:
        result -= heapq.heappop(possible_jewels)  # 음수로 저장된 값을 다시 양수로 변경해서 더함

print(result)
