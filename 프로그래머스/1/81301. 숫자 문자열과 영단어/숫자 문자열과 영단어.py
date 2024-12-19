def solution(s):
    idx = 0
    answer = ""
    word = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4","five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        else:
            for key in word:
                if s[idx:idx+len(key)] == key:
                    answer += word[key]
                    idx += len(key)
                    break
    return int(answer)
