N, K = map(int,input().split())
A = list(map(int, input().split()))
A.sort()
# end는 뒤에서 부터 하면 되네
start = 0
cnt = 0
for e in range(N-1,-1,-1):
    if start >= e:
        break
    if A[e] + A[start] <= K:
        start += 1
        cnt += 1
print(cnt)
