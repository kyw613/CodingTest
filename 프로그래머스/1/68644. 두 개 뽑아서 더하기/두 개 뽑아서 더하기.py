from itertools import combinations
def solution(numbers):
    result = []
    array = list(combinations(numbers,2))
    for r1,r2 in array:
        if r1+r2 in result:
            continue
        else:
            result.append(r1+r2)
    return sorted(result)
    