import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))
# 현재채널
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)
