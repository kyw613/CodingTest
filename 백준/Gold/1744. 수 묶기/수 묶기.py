N = int(input())
arr_up = []
arr_down = []
cnt_0 = 0
total = 0
for _ in range(N):
    a = int(input())
    if a == 0:
        cnt_0 += 1
    elif a>0:
        if a == 1:
            total += 1
        else:
            arr_up.append(a)
    elif a<0:
        arr_down.append(a)
arr_up.sort(reverse=True)
arr_down.sort()
if len(arr_up) % 2 == 0:
    for i in range(0,len(arr_up)-1,2):
        total += arr_up[i]*arr_up[i+1]
else:
    for i in range(0,len(arr_up)-2,2):
        total += arr_up[i]*arr_up[i+1]
    total += arr_up[-1]

if len(arr_down) % 2 == 0:
    for i in range(0,len(arr_down)-1,2):
        total += arr_down[i]*arr_down[i+1]
else:
    for i in range(0,len(arr_down)-2,2):
        total += arr_down[i]*arr_down[i+1]
    if cnt_0 <=0:
        total += arr_down[-1]
print(total)

