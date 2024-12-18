def solution(absolutes, signs):
    total = 0
    for a,s in zip(absolutes,signs):
        if s:
            total += a
        else:
            total -= a
    return total
        