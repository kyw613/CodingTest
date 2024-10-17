N = int(input())
A = list(map(int, input().split()))

A.sort()  # 투포인터 사용을 위해 정렬

good_count = 0

# 각 숫자를 다른 두 숫자의 합으로 만들 수 있는지 확인
for i in range(N):
    target = A[i]
    left, right = 0, N - 1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        
        current_sum = A[left] + A[right]
        
        if current_sum == target:
            good_count += 1
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1

print(good_count)
