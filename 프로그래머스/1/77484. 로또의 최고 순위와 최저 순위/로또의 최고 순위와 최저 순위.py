def solution(lottos, win_nums):
    #0인거 갯수 세고 0인거 빼고 win_num이랑 비교후 더한게 최고 다 틀린게 최저
    score = {"6":1,"5":2,"4":3,"3":4,"2":5}
    cnt = 0
    cnt_0 = 0
    result = []
    for i in lottos:
        if i == 0:
            cnt_0 += 1
            continue
        else:
            if i in win_nums:
                cnt += 1
    max_num = str(cnt + cnt_0)
    if max_num in score.keys():
        max_rate = score[max_num]
    else:
        max_rate = 6
        
    if max_rate + cnt_0 >= 6:
        min_rate = 6
    else:
        min_rate = max_rate + cnt_0
    result.append(max_rate)
    result.append(min_rate)
    return result
    