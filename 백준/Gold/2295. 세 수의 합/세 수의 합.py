import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort() # 오름차순
S = set()
for x in A:
    for y in A:
        S.add(x+y)

# 두개를 더한게들어감! 그러면 이제 이분탐색으로 하면 되겠다!
T = False
for i in range(N-1,-1,-1):
    if T:
        break
    for j in range(i+1):
        if (A[i] - A[j]) in S:
            print(A[i])
            T = True
            break
