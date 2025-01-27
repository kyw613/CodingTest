def solution(citations):
    citations.sort(reverse=True)
    for i, k in enumerate(citations):
        if i + 1 > k:  # 논문의 순서 > 인용 수
            return i # 이 시점을 만족하는 값이 없음..
    return len(citations)  # 모든 논문이 조건을 만족