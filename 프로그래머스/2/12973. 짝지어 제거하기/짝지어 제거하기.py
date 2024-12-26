def solution(s):
    stack = []
    for word in s:
        stack.append(word)
        if len(stack) <= 1:
            continue
        if stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
    if stack:
        return 0
    else:
        return 1
        