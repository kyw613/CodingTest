def solution(n, lost, reserve):
    set_reserve = [r for r in reserve if r not in lost]
    set_lost = [l for l in lost if l not in reserve]
    set_lost.sort()
    set_reserve.sort()

    for i in range(len(set_reserve)):
        if set_reserve[i] > 1:
            if (set_reserve[i] -1) in set_lost:
                set_lost.remove(set_reserve[i]-1)
                continue
        if set_reserve[i] < n:
            if (set_reserve[i] + 1) in set_lost:
                set_lost.remove(set_reserve[i]+1)
    return n - len(set_lost)
        
                        
