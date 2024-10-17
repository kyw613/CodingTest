N, M = map(int, input().split())
A = list(map(int, input().split()))
#초기값!
total = sum(A[:M])
max_val = total
for i in range(1,N-M+1):
    total -= A[i-1]
    total += A[i+M-1]
    max_val = max(max_val,total)
print(max_val)