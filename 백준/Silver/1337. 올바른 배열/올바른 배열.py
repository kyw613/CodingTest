N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
max_cnt = 1

for s in range(N-1):
    cnt = 1
    val = A[s]
    i = s
    while True:
        if A[i+1] <= val+4:
            cnt += 1
            i += 1
            if i >= N-1:
                break
        else:
            break
    max_cnt = max(max_cnt,cnt)
print(5-max_cnt)