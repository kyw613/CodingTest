N, M = map(int, input().split())
# i부터 j까지의 합이 M
A = list(map(int, input().split()))
start = 0
s = 0
cnt = 0
for e in range(N):
    #크면 start를 늘리고 작으면 end를 늘린다!
    s += A[e] # 뒤에꺼 더하고
    if s > M:
        while s > M:
            s -= A[start]
            start += 1
    if s == M:
        cnt += 1
print(cnt)
