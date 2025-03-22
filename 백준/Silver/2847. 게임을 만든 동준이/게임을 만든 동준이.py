N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

cnt = 0
comp = 0
for i in range(len(arr)-1,-1,-1):
    if i == len(arr)-1:
        comp = arr[i]
        continue
    if arr[i] >= comp:
        comp -= 1
        cnt += -comp +arr[i]
    else:
        comp = arr[i]
print(cnt)

