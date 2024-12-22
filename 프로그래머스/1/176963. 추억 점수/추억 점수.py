def solution(name, yearning, photo):
    score = {n: y for n, y in zip(name, yearning)}
    result = []
    for i in range(len(photo)):
        answer = 0
        for k in photo[i]:
            if k in score:
                answer += score[k]
        result.append(answer)
    return result

