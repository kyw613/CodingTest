def solution(a, b):
    total = 0
    for k in range(len(a)):
        total += a[k] * b[k]
    return total