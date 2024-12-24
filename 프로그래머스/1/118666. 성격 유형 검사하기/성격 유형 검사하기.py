def solution(survey, choices):
    result = ""
    score = {1:-3,2:-2,3:-1,4:0,5:1,6:2,7:3}
    pri = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for sur,c in zip(survey,choices):
        pri[sur[1]] += score[c]
    print(pri)
    if pri["R"] >= pri["T"]:
        result += "R"
    else:
        result += "T"
    if pri["C"] >= pri["F"]:
        result += "C"
    else:
        result += "F"
    if pri["J"] >= pri["M"]:
        result += "J"
    else:
        result += "M"
    if pri["A"] >= pri["N"]:
        result += "A"
    else:
        result += "N"
    return result
        