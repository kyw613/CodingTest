def solution(s, skip, index):
    result = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        idx = ord(s[i]) - ord("a")
        cnt = 0
        while True:
            if cnt == index:
                break
            if alpha[(idx+cnt+1)%26] in skip:
                idx += 1
                continue
            else:
                cnt += 1
        result += alpha[(idx+cnt)%26]
    return result
        
            
        
        