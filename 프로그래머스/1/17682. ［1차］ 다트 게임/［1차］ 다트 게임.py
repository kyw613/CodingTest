def solution(dartResult):
    #1. s,d,t에다라 저장
    #2. *#에의해 점수가 달라짐.. 그러면 기존 점수를 저장하고 있어야함
    #즉 점수에 *#이 나올때마다 달라진것을 다시 결과에 저장하고 마지막에 더해주기.
    idx = 0
    result = [0] * 3
    nums = "1234567890"
    for i in range(3):
        if dartResult[idx] in nums:
            if dartResult[idx] == "1" and dartResult[idx + 1] == "0":
                result[i] = 10
                idx += 2
            else:
                result[i] = int(dartResult[idx])
                idx += 1
        if dartResult[idx] == "S":
            idx += 1
        elif dartResult[idx] == "D":
            result[i] = result[i] ** 2
            idx += 1
        elif dartResult[idx] == "T":
            result[i] = result[i] ** 3
            idx +=1
        if idx > len(dartResult) -1:
            break
        if dartResult[idx] == "*":
            if i ==0:
                result[i] = result[i] * 2
                idx += 1
            else:
                result[i-1] = result[i-1] * 2
                result[i] = result[i] * 2
                idx += 1
        elif dartResult[idx] == "#":
                result[i] = result[i] * (-1)
                idx += 1
    return sum(result)

        
            
            
        
            
                
                
        