def solution(d, budget):
    d = sorted(d)
    type_s = False
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            type_s = True
            break
    if type_s:
        return i
    else:
        return i+1