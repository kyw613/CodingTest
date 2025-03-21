N = int(input())
arr = list(map(int,input().split()))
save = []
for i in range(N):
    if arr[i] <0:
        save.append((-arr[i],-1))
    else:
        save.append((arr[i],1))
save.sort()
max_val = 1000000000000
pos = (0,0)
for x in range(0,N-1):
    total = abs(save[x][0]*save[x][1] + save[x+1][0]*save[x+1][1])
    if total < max_val:
        max_val = total
        a=save[x][0]*save[x][1]
        b=save[x+1][0]*save[x+1][1]
if a>b:
    a,b = b,a
print(a,b)




