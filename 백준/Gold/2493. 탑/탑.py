N = int(input())
number = list(map(int,input().split()))

stack = []
ans = [0] * N
for i in range(N):
    val = number[i]
    while stack and stack[-1][1] < val:
        stack.pop()
    if stack:
        ans[i] = stack[-1][0] + 1
    stack.append((i,val))
print(*ans)