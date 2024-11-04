def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

T = int(input())
for _ in range(T):  
    N, M = map(int,input().split())# 이때 n<=m 만족
    cnt = factorial(M) // (factorial(N) * factorial(M-N))
    print(cnt)