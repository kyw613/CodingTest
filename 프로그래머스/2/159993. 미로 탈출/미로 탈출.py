from collections import deque

def bfs(visit,maps,pos,target):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visit[pos[0]][pos[1]] = True
    queue = deque([(0,pos[0],pos[1])])
    size_y = len(maps)
    size_x = len(maps[0])
    while queue:
        idx,y,x = queue.popleft()
        for i in range(4):
            ny,nx = y + dy[i],x + dx[i]
            if 0<=ny< size_y and 0 <= nx < size_x and visit[ny][nx] == False and maps[ny][nx] != "X":
                if (ny,nx) == target:
                    return idx + 1
                visit[ny][nx] = True
                queue.append((idx+1,ny,nx))
    return False
                

def solution(maps):
    #일단 start(S)와 L그리고 E(exit)의 위치를 아는게 첫번째고
    # bfs를 사용하여 start -> L
    # 그리고 bfs를 사용하여 L -> Exit으로 가는것이 중요 
    # 이때 visit을 초기화 하면 될듯
    #1. S,L,E 고르기
    for i in range(len(maps)):
        if "S" in maps[i]:
            for w in range(len(maps[i])):
                if maps[i][w] == "S":
                    start = (i,w)
                    break
        if "L" in maps[i]:
            for w in range(len(maps[i])):
                if maps[i][w] == "L":
                    loop = (i,w)
                    break
        if "E" in maps[i]:
            for w in range(len(maps[i])):
                if maps[i][w] == "E":
                    end = (i,w)
                    break
    # 이제 start에서 loop까지 가는데 필요한 cnt구하기
    cnt = 0
    visit = [[False] * len(maps[0]) for _ in range(len(maps))]

    val = bfs(visit,maps,start,loop)
    if val == False:
        return -1
    else:
        cnt += val
    visit = [[False] * len(maps[0]) for _ in range(len(maps))]
    val2 = bfs(visit,maps,loop,end)
    if val2 == False:
        return -1
    else:
        cnt += val2
    return cnt
    
        