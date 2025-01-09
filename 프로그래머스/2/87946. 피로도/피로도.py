from itertools import permutations
def solution(k, dungeons):
    turn = list(permutations(dungeons,len(dungeons)))
    max_cnt = -1
    for i in turn:
        total = k
        cnt = 0
        for t in range(len(dungeons)):
            if total >= i[t][0]:
                total -= i[t][1]
                cnt += 1
        max_cnt = max(max_cnt,cnt)
    return max_cnt
            