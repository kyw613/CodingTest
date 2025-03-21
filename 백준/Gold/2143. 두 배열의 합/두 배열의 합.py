T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
A_sum = {}
for i in range(n):
    for j in range(i,n):
        if sum(A[i:j+1]) not in A_sum:
            A_sum[sum(A[i:j+1])] = 1
        else:
            A_sum[sum(A[i:j+1])] += 1
B_sum = {}
for i in range(m):
    for j in range(i,m):
        if sum(B[i:j+1]) not in B_sum:
            B_sum[sum(B[i:j+1])] = 1
        else:
            B_sum[sum(B[i:j+1])] += 1
#이거 sort후 이진탐색 하자.
AA = sorted(A_sum.items())
BB = sorted(B_sum.items())
right_idx = 0
left_idx = len(BB)-1
result = 0
while right_idx <= len(AA)-1 and left_idx >= 0:
    total = AA[right_idx][0] + BB[left_idx][0]
    if total > T:
        left_idx -= 1
    elif total < T:
        right_idx += 1
    elif total == T:
        result += AA[right_idx][1] * BB[left_idx][1]
        left_idx -= 1
        right_idx += 1
print(result)
         
