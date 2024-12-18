def solution(n):
    answer = ""
    total = 0
    # 먼저 최대 길이를 정해야하잖아...
    #100000000이하의 자연수면  3의 16승 이하일듯?
    for i in range(16,-1,-1):
        for k in range(2,-1,-1):
            if n >= 3**i * k:
                n -= 3**i * k
                answer += str(k)
                break
    #answer 앞에 0 없애기
    for z in range(len(answer)):
        if answer[z] != "0":
            cnt = z
            break
    answer = str(answer)
    #뒤집기
    answer = answer[z:]
    answer = answer[::-1]
    for x in range(len(answer)):
        total += 3 ** (len(answer)-x-1) * int(answer[x])
    return total

    

            
        
            