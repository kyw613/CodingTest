N, K = map(int, input().split())
A = list(map(int, input().split()))
dic = {}
# 1을 k개 이상을 포함하는 가장 작은 집합!
min_val = len(A)+1
start = 0
for e in range(len(A)):
    if not A[e] in dic:
        dic[A[e]] = 1
    else:
        dic[A[e]] += 1

    if  A[e] == 1 and dic[A[e]] >= K:
        while True:
            if A[start] == 1:
                break
            dic[A[start]] -= 1
            start += 1
        # start는 딱 그 순간꺼
        dist = e - start + 1
        dic[A[start]] -= 1
        start += 1
        min_val = min(min_val,dist)

if min_val == len(A) + 1:
    print("-1")
else:
    print(min_val)

    
    
