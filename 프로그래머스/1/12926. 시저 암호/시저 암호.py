def solution(s, n):
    #대문자 소문자따로 설정
    #대문자
    answer = ""
    for k in range(len(s)):
        if s[k].isupper():
            answer += chr( ord("A") + (ord(s[k]) - ord("A") + n ) % 26 )
        elif s[k].islower():
            answer += chr(ord("a") + (ord(s[k]) - ord("a")+ n ) % 26) 
        else:
            answer += s[k]
    return answer