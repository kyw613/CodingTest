def solution(s):
    prev = {}
    result = []
    for i in range(len(s)):
        if not s[i] in prev:
            result.append(-1)
            prev[s[i]] = i
        else:
            result.append(i-prev[s[i]])
            prev[s[i]] = i
            
    return result   
