from collections import deque
T = int(input())
for _ in range(T):
    leng = int(input())
    s_x,s_y = map(int,input().split())
    q = deque([(0,s_x,s_y) ]) 
    e_x,e_y = map(int,input().split())
    end = (s_x,s_y)
    visit = [[True]* leng for _ in range(leng)]
    step = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)]
    visit[s_x][s_y] = False
    while q:
        idx,s_x,s_y = q.popleft()
        if s_x == e_x and s_y == e_y:
            print(idx)
            break
        for i in range(8):
            nx = step[i][0] + s_x 
            ny = step[i][1] + s_y
            if 0<= nx < leng and 0 <= ny < leng and visit[nx][ny] == True:
                visit[nx][ny] = False
                q.append((idx+1,nx,ny))


