T = int(input())
for tc in range(T):
    arr = list(map(int,input().split()))
    arr.pop(0)
    #arr -> 1부터 음 ()
    stack = {}
    for a in arr:
        stack[a] = 0
        for s in stack.keys():
            if a < s:
                stack[s] += 1
    print(tc+1,sum(stack.values()))

    