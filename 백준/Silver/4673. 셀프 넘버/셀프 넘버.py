# 각 숫자를 증가시키고 이때마다 다 확인?
# 재귀를 사용하면 편할듯 list에 다 True를 넣어놓고 반복해서 False로 바꾸는거야
# 그래서 마지막에 True를 출력하게 하면 되네.
N = 10001
A = [True] * N# 0부터 10000까지

for i in range(1,N):
    idx = i
    if A[i] == False:
        continue
    else:
        while True:
            total = idx
            ch = str(idx)
            for i in ch:
                total += int(i)
            if total >= N:
                break
            elif A[total] == False:
                break
            else:
                A[total] = False
                idx = total


for t in range(1,len(A)):
    if A[t] == True:
        print(t)

