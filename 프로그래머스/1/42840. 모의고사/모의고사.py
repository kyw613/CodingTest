def solution(answers):
    # 수포자들의 패턴 정의
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]  # 수포자 1, 2, 3의 점수
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            score[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            score[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            score[2] += 1
    
    # 가장 높은 점수를 받은 수포자
    max_score = max(score)
    result = []
    for i in range(3):
        if score[i] == max_score:
            result.append(i + 1)  
    
    return result
