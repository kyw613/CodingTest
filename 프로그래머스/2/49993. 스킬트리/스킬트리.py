def solution(skill, skill_trees):
    #선행스킬...
    # 스킬에 스킬트리를 주고
    # C다음에 B다음에 D가 나와야 하는거야..
    skill_dict = {}
    for s in skill:
        skill_dict[s] = 1
    cnt = 0
    for skill_tree in skill_trees:
        idx = 0
        ty = False
        for st in skill_tree:
            if st in skill_dict:
                if skill[idx] != st:
                    ty = True
                    break
                else:
                    idx += 1
        if ty == False:
            cnt += 1
    return cnt
                
            
            