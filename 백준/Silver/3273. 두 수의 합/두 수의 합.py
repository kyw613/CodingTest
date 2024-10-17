N = int(input())
A = list(map(int, input().split()))
X = int(input())
A.sort()
cnt = 0
total = 0
# 이걸 정렬했으니까 end를 1~N까지 하고 그때 start하면 되네
for s in range(N):
    total = A[s]
    for j in range(s+1,N):
        if total + A[j] == X:
            cnt += 1
        elif total + A[j] > X:
            break
print(cnt)
    
