K,N = map(int,input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
arr.sort()
s ,e = 0,max(arr)
while s<=e:
    mid = (s+e)//2
    cnt = 0
    if mid == 0:
        e += 1
    else:
        for a in arr:
            cnt += a//mid
        if cnt >= N:
            answer = mid
            s = mid + 1
        elif cnt < N:
            e = mid - 1
        
print(answer)


