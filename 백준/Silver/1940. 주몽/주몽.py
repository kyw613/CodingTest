N = int(input()) # 개수
M = int(input()) # 합
A = list(map(int, input().split()))
A.sort()
start = 0
end = N-1
cnt = 0
while start < end:
    s = A[start] + A[end]
    if s > M:
        end -= 1
    elif s == M:
        cnt += 1
        start += 1
        end -= 1
    elif s < M:
        start += 1

print(cnt)


