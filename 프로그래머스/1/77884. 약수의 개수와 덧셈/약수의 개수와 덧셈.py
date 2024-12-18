def solution(left, right):
    total = 0
    for i in range(left,right+1):
        cnt = 0
        for k in range(1,int(i**0.5)+1):
            if i % k ==0:
                cnt += 2
                if k == i //k:
                    cnt -= 1
        if cnt % 2 :
            total -= i
        else:
            total += i
    return total