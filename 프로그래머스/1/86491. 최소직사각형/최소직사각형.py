def solution(sizes):
    max_width = 0
    max_height = 0
    
    for w, h in sizes:
        # 명함의 가로와 세로 중 더 작은 값을 가로, 더 큰 값을 세로로 정렬
        if w < h:
            w, h = h, w
        # 가장 큰 가로 길이와 가장 큰 세로 길이를 업데이트
        max_width = max(max_width, w)
        max_height = max(max_height, h)
    return max_width * max_height