from collections import deque

def bfs(y,x):
    comp = arr[y][x]
    q = deque([(y,x)])
    visit[y][x] = False
    cnt = 1
    r_cnt = 0
    rainbow_list = []
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 0 and visit[ny][nx]:
                    r_cnt += 1
                    cnt += 1
                    visit[ny][nx] = False
                    q.append((ny,nx))
                    rainbow_list.append((ny,nx))
                elif arr[ny][nx] == comp and visit[ny][nx]:
                    cnt += 1
                    visit[ny][nx] = False
                    q.append((ny,nx))
    for p in rainbow_list:
        visit[p[0]][p[1]] = True
    return cnt,r_cnt


def del_bfs(y,x):
    comp = arr[y][x]
    q = deque([(y,x)])
    visit[y][x] = False
    arr[y][x] = -2
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 0 and visit[ny][nx]:
                    visit[ny][nx] = False
                    arr[ny][nx] = -2
                    q.append((ny,nx))
                elif arr[ny][nx] == comp and visit[ny][nx]:
                    arr[ny][nx] = -2
                    visit[ny][nx] = False
                    q.append((ny,nx))


def gravity(arr):
    for x in range(N):
        for y in range(N-2, -1, -1):
            if arr[y][x] >= 0:
                ny = y
                while True:
                    if 0 <= ny + 1 < N and arr[ny+1][x] == -2:
                        arr[ny+1][x], arr[ny][x] = arr[ny][x], -2
                        ny += 1
                    else:
                        break


def rotate(arr):
    size = len(arr)
    new_arr = [[0] * size for _ in range(size)]
    
    for y in range(size):
        for x in range(size):
            new_arr[size - x - 1][y] = arr[y][x]

    return new_arr
    


#main
N,M = map(int,input().split()) #N은 격자수 M은 일반블록 갯수
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
answer = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]

while True:
    visit = [[True]* N for _ in range(N)]
    max_cnt = 0
    max_r_cnt = 0
    pos = (-1,-1)
    ty = False
    for y in range(N):
        for x in range(N):
            if arr[y][x] >0 and visit[y][x] == True:
                cnt,rainbow_cnt = bfs(y,x)
                if cnt < 2:
                    continue
                ty = True
                if max_cnt < cnt:
                    max_r_cnt = rainbow_cnt
                    max_cnt = cnt
                    pos = (y,x)
                elif max_cnt == cnt:
                    if max_r_cnt < rainbow_cnt:
                        max_r_cnt = rainbow_cnt
                        pos = (y,x)
                    elif max_r_cnt == rainbow_cnt:
                        if pos[0] < y:
                            pos = (y,x)
                        elif pos[0] == y and pos[1] < x:
                            pos = (y,x)

    if ty == False:
        break
    answer += max_cnt**2
    visit = [[True]* N for _ in range(N)]
    del_bfs(pos[0],pos[1])

    gravity(arr)

    arr = rotate(arr)

    gravity(arr)
print(answer)