def solution(keymap, targets):
    #그냥 쉽게 2개의 자판에서 나오는 최솟값 저장
    result = []
    cnt = 0
    for target in targets:
        total = 0
        ty = False
        for i in range(len(target)):
            min_val = 101
            for key in keymap:
                for t in range(len(key)):
                    if key[t] == target[i]:
                        min_val = min(min_val,t+1)
                        break
            if min_val == 101:
                ty = True
                result.append(-1)
                break
            total += min_val
        if ty:
            continue
        result.append(total)
    return result
                    
                    
        
        