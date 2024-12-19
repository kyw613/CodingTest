def solution(sizes):
    #큰거 왼쪽 작은거 오른쪽 정렬후 최대찾아서 곱하기
    max_right = 0
    max_left = 0
    
    for k in range(len(sizes)):
        if sizes[k][0] <= sizes[k][1]:
            sizes[k][0], sizes[k][1] = sizes[k][1], sizes[k][0]
        max_right = max(max_right,sizes[k][1])
        max_left = max(max_left,sizes[k][0])
    
    return max_right * max_left
        