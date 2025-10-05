import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break

    n = nums[0]
    heights = nums[1:]
    stack = []
    best = 0

    # 마지막에 0 추가해 스택 비우기
    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > h:
            idx, hh = stack.pop()
            area = hh * (i - idx)
            if area > best:
                best = area
            start = idx
        stack.append((start, h))

    print(best)
