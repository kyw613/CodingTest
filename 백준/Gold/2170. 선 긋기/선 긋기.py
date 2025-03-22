N = int(input())
arr = []
for _ in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x:(x[0],-x[1])) # 뒤에는 큰거로 하자
s_comp ,e_comp= arr[0][0],arr[0][1]
total = 0
for i in range(1,N):
    s_val,e_val = arr[i][0],arr[i][1]
    if e_comp >= s_val:
        e_comp = max(e_comp,e_val)
    else:
        total += e_comp-s_comp
        s_comp,e_comp = s_val,e_val

total += e_comp-s_comp
print(total)



