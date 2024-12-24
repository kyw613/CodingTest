4
5
6
7
8
9
10
11
12
13
14
15
16
17
def solution(X, Y):
    from collections import Counter

    couple = Counter(X) & Counter(Y)
    if not couple:
        return "-1"

    _sorted = sorted(couple.items(), key=lambda x: -int(x[0]))
    if _sorted[0][0] == "0":
        return "0"

    answer = []
    for k, v in _sorted:
        answer.append(k * v)

    return "".join(answer)