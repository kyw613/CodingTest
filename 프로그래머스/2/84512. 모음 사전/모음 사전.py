def solution(word):
    result = 0
    comp = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    weights = [781, 156, 31, 6, 1]  # 각 자리의 가중치

    # 각 자리의 문자를 확인하며 가중치를 곱해 계산
    for i in range(len(word)):
        char = word[i]
        # 각 자리의 가중치를 적용하여 더해줌
        result += (comp[char] - 1) * weights[i] + 1

    return result