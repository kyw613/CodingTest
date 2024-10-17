import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = []
for j in range(N):
    g, x = map(int, input().split())
    A.append([x, g])  # 위치, 얼음 저장

# 얼음 위치 기준으로 정렬
A.sort(key=lambda x: x[0])

# 슬라이딩 윈도우 변수 초기화
max_val = 0
current_ice = 0
left = 0

# 슬라이딩 윈도우로 범위 내 얼음의 합 계산
for right in range(N):
    # A[right][0]이 현재 창의 범위 안에 있는지 확인 (왼쪽 끝은 A[left][0])
    current_ice += A[right][1]  # 오른쪽 창을 확장하면서 얼음 더하기
    
    # 창의 범위가 2K를 넘는지 확인, 넘으면 창의 왼쪽을 줄여나감
    while A[right][0] - A[left][0] > 2 * K:
        current_ice -= A[left][1]  # 왼쪽 창을 줄이면서 얼음 빼기
        left += 1

    # 현재 창에서의 최대 얼음 합 갱신
    max_val = max(max_val, current_ice)

print(max_val)
