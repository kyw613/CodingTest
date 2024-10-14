import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # N은 칭호 개수, M은 비교 개수
A = []

for _ in range(N):
    name, score = input().split()
    A.append((name, int(score)))


A.sort(key=lambda x: x[1])

# 이분 탐색 시작
for _ in range(M):
    comp = int(input())
    start = 0
    end = N - 1
    result = ""

    while start <= end:
        mid = (start + end) // 2
        if comp <= A[mid][1]:
            result = A[mid][0]
            end = mid - 1
        else:
            start = mid + 1

    # 결과 출력
    print(result)
