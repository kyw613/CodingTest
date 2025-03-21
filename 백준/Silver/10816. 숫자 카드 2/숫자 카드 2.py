N = int(input())
arr = list(map(int,input().split()))
num = {}
for a in arr:
    a = str(a)
    if a not in num:
        num[a] = 1
    else:
        num[a] += 1
M = int(input())
arr = list(map(int,input().split()))
result = []
for a in arr:
    a = str(a)
    if a in num:
        result.append(num[a])
    else:
        result.append(0)
print(" ".join(map(str,result)))