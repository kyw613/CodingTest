N,K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s,e = 0,max(arr)
while s<=e:
    mid = (s+e)//2
    total = 0
    for i in range(N-1,-1,-1):
        if arr[i] > mid:
            total += arr[i]-mid
        else:
            break
    if total > K:
        s = mid+1
        answer = mid
    if total < K:
        e = mid - 1
    if total == K:
        answer = mid
        break
print(answer)




