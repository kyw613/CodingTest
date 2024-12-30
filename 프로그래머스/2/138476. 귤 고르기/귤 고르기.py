from collections import Counter
def solution(k, tangerine):
    # 서로 다른종류 최소화 -> count후 sort하기
    # 서로 다른 값 return 하기
    c = (Counter(tangerine))
    val = (sorted(c.items(),reverse = True, key=lambda x:x[1]))
    cnt = 1
    total = 0
    for _,v in val:
        total += int(v)
        if total >= k:
            return cnt
        else:
            cnt += 1
        