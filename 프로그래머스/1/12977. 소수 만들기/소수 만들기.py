from itertools import combinations
def solution(nums):
    result = 0
    totals = []
    #combinations 이용해 3개 더하고 중복제거
    array = list(combinations(nums,3))
    for a,b,c in array:
        totals.append(a+b+c)
    for k in totals:
        ty = True
        for t in range(2,int(k**0.5)+1):
            if k % t == 0:
                ty = False
                break
        if ty:
            result += 1
    return result