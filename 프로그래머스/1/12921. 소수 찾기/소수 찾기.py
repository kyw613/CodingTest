def solution(n):
    if n == 1:
        return 0
    result = 0
    for i in range(2,n+1):
        ty = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                ty = False
                break
        if ty:
            result += 1
    return result
        
        
        
    