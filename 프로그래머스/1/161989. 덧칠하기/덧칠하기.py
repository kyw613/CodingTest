def solution(n, m, section):
    cnt = 0
    current_position = section[0]  

    for pos in section:
        if pos >= current_position:  #
            cnt += 1
            current_position = pos + m  # 페인트 칠할 범위를 이동

    return cnt
