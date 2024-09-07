def solution(x, n):
    answer = []
    init = x
    for i in range(n):
        answer.append(x)
        x += init
    return answer
        