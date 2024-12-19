def solution(n):
    #연속된 자연수 -> 큰거부터 차례로
    cnt = 0
    total = 0
    pre = []
    
    for i in range(n,0,-1):
        total += i
        pre.append(i)
        if total == n:
            cnt += 1
        elif total > n:
            fin = pre.pop(0)
            total -= fin
    return cnt
        
        
        