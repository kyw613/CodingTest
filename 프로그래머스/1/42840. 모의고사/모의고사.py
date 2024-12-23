def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    result = []
    total1 = 0
    total2 = 0
    total3 = 0
    for k in range(len(answers)):
        if answers[k] == pattern1[k%5]:
            total1 += 1
        if answers[k] == pattern2[k%8]:
            total2 += 1
        if answers[k] == pattern3[k%10]:
            total3 += 1
    max_val = max(total1,total2,total3)
    if total1 == max_val:
        result.append(1)
    if total2 == max_val:
        result.append(2)
    if total3 == max_val:
        result.append(3)
    return result
    
    
                
            