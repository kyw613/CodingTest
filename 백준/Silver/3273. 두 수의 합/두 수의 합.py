N = int(input())
A = list(map(int, input().split()))
X = int(input())

A.sort()
cnt = 0
start, end = 0, N - 1

while start < end:
    total = A[start] + A[end]
    
    if total == X:
        cnt += 1
        start += 1
        end -= 1
    elif total < X:
        start += 1  # 합이 X보다 작으면 start를 증가시켜 더 큰 값을 탐색
    else:
        end -= 1  # 합이 X보다 크면 end를 감소시켜 더 작은 값을 탐색

print(cnt)
