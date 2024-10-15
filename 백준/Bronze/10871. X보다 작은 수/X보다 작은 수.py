import sys
input = sys.stdin.readline
#첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다
N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for num in A:
    if num < X:
        result.append(str(num))
res = " ".join(result)
print(res)