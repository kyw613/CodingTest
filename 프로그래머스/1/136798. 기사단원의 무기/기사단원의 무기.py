def solution(number, limit, power):
    divided = []
    result = 0
    for i in range(1,number+1):
        total = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                total += 2
                if i // j == j:
                    total -= 1
        divided.append(total)
    for k in divided:
        if limit < k:
            result += power
        else:
            result += k
    return result
    
        