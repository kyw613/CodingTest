N = int(input())
A = {}
Ar = []
total = 0
cnt = 0

def custom_round(value):
    integer_part = int(value)
    decimal_part = value - integer_part
    
    if decimal_part < 0.5:
        return integer_part  # 4 이하 버림
    elif decimal_part > 0.5:
        return integer_part + 1  # 6 이상 올림
    else:  # 5인 경우
        if integer_part % 2 == 0:
            return integer_part + 1  # 짝수일 경우 올림(가까운 홀수로)
        else:
            return integer_part  # 홀수인 경우 그대로 유지
        
        
for _ in range(N):
    data = int(input())
    total += data
    cnt += 1
    Ar.append(data)
    if not data in A:
        A[data] = 1
    else:
        A[data] += 1
#1. 평균
average =round(total / cnt)
print(average)
#2. 중앙값.
Ar.sort()

mid = N // 2
print(Ar[mid])

#3. 최빈값..
Array = list(sorted(A.items(),key=lambda x:(-x[1],x[0])))
max_val = Array[0][1]
cnt_val = 0
result = []
for k,v in Array:
    if v == max_val:
        cnt_val += 1
        result.append(k)

if cnt_val <= 1:
    print(result[0])
elif cnt_val >= 2:
    print(result[1])
#4. len
print(Ar[-1] - Ar[0])
