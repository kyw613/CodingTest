import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 회전처리
A = A * 2

count = [0] * (d+1)
cnt = 0

# 첫 k개 초밥
for i in range(k):
    if count[A[i]] == 0:
        cnt += 1
    count[A[i]] += 1

# 쿠폰 초밥이 포함되지 않으면 +1
max_cnt = cnt
if count[c] == 0:
    max_cnt += 1

for i in range(1, N):
    removed_sushi = A[i-1]
    count[removed_sushi] -= 1
    if count[removed_sushi] == 0:
        cnt -= 1
    
    # 새로운 초밥 추가
    new_sushi = A[i+k-1]
    if count[new_sushi] == 0:
        cnt += 1
    count[new_sushi] += 1

    # 쿠폰 초밥 포함 여부 확인
    coupon_sushi = 1 if count[c] == 0 else 0
    max_cnt = max(max_cnt, cnt + coupon_sushi)

print(max_cnt)
