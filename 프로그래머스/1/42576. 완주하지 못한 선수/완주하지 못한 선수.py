def solution(participant, completion):
    name_dict = {}
    answer = ""
    for i,name in enumerate(participant):
        if name not in name_dict:
            name_dict[name] = 1
        else:
            name_dict[name] += 1
    for t in completion:
        if t in name_dict:
            name_dict[t] -= 1
    s = sorted(name_dict.items(),key=lambda x:-x[1])
    answer += s[0][0]
    return answer