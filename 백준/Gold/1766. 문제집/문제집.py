import heapq
import sys

input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())
order = {i: [] for i in range(1, N+1)}  # 각 문제에 대한 선행 문제 리스트
indegree = {i: 0 for i in range(1, N+1)}  # 진입 차수 (0이면 바로 풀 수 있음)

# 선행 문제 관계 입력
for _ in range(K):
    a, b = map(int, input().split())  # b를 풀기 전에 a를 먼저 풀어야 함
    order[a].append(b)  # a -> b 관계 저장
    indegree[b] += 1  # b의 진입 차수 증가

# 우선순위 큐를 이용한 위상 정렬
q = []
for i in range(1, N+1):
    if indegree[i] == 0:  # 진입 차수가 0인 문제부터 시작
        heapq.heappush(q, i)

result = []

while q:
    now = heapq.heappop(q)  # 현재 풀 수 있는 문제 중 가장 작은 번호 선택
    result.append(now)

    for next_problem in order[now]:  # 현재 문제를 풀고 나면 풀 수 있는 문제들 확인
        indegree[next_problem] -= 1
        if indegree[next_problem] == 0:  # 진입 차수가 0이 되면 큐에 삽입
            heapq.heappush(q, next_problem)

# 결과 출력
print(" ".join(map(str, result)))
