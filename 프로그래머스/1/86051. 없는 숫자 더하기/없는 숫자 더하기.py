def solution(numbers):
    array = [0] * 10
    total = 0
    for i in numbers:
        array[i] += 1
    for k in range(10):
        if array[k] == 0:
            total += k
    return total