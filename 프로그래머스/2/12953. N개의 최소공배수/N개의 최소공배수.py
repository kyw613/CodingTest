def solution(arr):
    #가장 쉬운방법은 있음
    init = max(arr)
    max_val = 0
    while True:
        max_val += init
        ty = False
        for k in arr:
            if max_val % k:
                ty = True
                break
        if not ty:
            return max_val
        
