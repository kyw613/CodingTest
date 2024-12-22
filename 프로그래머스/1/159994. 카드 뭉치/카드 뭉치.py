def solution(cards1, cards2, goal):
    for i in goal:
        if cards1:
            if cards1[0] == i:
                cards1.pop(0)
                continue
        if cards2:
            if cards2[0] == i:
                cards2.pop(0)
                continue
        return "No"
    return "Yes"
    
