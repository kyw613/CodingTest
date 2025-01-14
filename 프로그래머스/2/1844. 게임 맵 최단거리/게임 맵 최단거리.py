from collections import deque
def solution(maps):
    # 1이 갈수 있는거 0이 벽 출발지점은 (0,0) 도착지점은(4,4)
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    row_len = len(maps)
    co_len = len(maps[0])
    visit = [[True] * co_len for _ in range(row_len)]
    array = deque([(1,0,0)])
    while array:
        idx,y,x = array.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0 <= ny <  row_len and 0 <=nx < co_len and maps[ny][nx] == 1 and visit[ny][nx] == True:
                visit[ny][nx] = False
                array.append((idx+1,ny,nx))
                if ny ==row_len-1 and nx ==co_len-1:
                    return idx+1
    return -1
                
    