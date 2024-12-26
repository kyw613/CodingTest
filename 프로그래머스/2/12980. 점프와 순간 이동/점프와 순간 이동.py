def solution(n):
    #한번에 k칸 점프 현재온거리 x2의 위치로 순간이동
    # 순간이동 건전지 사용량 x k칸 점프하면 k만큼의 건전지 사용량
    # N만큼 가려고할때 건전지 사용량 최소로 갈수 있나?
    cnt = 1
    while n != 1:
        if n % 2:
            n -= 1
            cnt += 1
        else:
            n = n // 2
    return cnt
        
        