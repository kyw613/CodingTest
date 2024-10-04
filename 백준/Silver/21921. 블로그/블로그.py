N, X = map(int,input().split())
cnt = 1
value = list(map(int,input().split()))
total = sum(value[:X])
max_val = total
if sum(value) ==0:
    print("SAD")
else:
    for i in range(1,N-X+1):
        total -= value[i-1]
        total += value[i+X-1]
        if total > max_val:
            max_val = total
            cnt = 1
        elif total == max_val:
            cnt += 1
    print(max_val)
    print(cnt)

