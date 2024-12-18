def solution(s):
    answer = ""
    cnt = 0
    for i in range(len(s)):
        if s[i] == " ":
            cnt = 0
            answer += s[i]
            continue
        if cnt > 0:
            answer += s[i].lower()
        if cnt == 0:
            if s[i].isalpha:
                answer += s[i].upper()
                cnt += 1

    return answer
                
        