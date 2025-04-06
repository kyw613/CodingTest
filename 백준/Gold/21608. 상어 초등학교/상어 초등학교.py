N = int(input())
graph = [[0]*N for _ in range(N)]
people = []
prefer = [[] for _ in range(N**2+1)]
step = [(-1,0),(0,1),(0,-1),(1,0)]
for _ in range(N**2):
    main,a,b,c,d = map(int,input().split())
    people.append(main)
    prefer[main].append(a)
    prefer[main].append(b)
    prefer[main].append(c)
    prefer[main].append(d)

for p in people:
    #1. 친한사람 많은순
    max_cnt = 0
    comp = []
    for y in range(N):
        for x in range(N):
            cnt = 0
            if graph[y][x] == 0:
                for i in range(4):
                    ny,nx = y+step[i][0],x + step[i][1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if graph[ny][nx] in prefer[p]:
                            cnt += 1
                if cnt >max_cnt:
                    max_cnt = cnt
                    comp = []
                    comp.append((y,x))
                elif cnt == max_cnt:
                    comp.append((y,x))
    if len(comp) == 1:
        y,x = comp[0][0],comp[0][1]
        graph[y][x] = p
        continue
    #print(p,comp)
    #2. list에 있는것중 공백 많은순
    max_cnt = 0
    comp2 = []
    for c in comp:
        y,x = c[0],c[1]
        cnt = 0
        for i in range(4):
            ny,nx =  y+step[i][0],x + step[i][1]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 0:
                    cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            comp2 = []
            comp2.append((y,x))
        elif cnt == max_cnt:
            comp2.append((y,x))
    if len(comp2) == 1:
        y,x = comp2[0][0],comp2[0][1]
        graph[y][x] = p 
        continue
    #3. 그중 제일 y,x가 가장 작은거 # 이렇게 할꺼면 걍 위에꺼처럼 할수 있긴 한데.
    comp2 = sorted(comp2)
    y,x = comp2[0][0],comp2[0][1]
    graph[y][x] = p

#만족도 구하기. 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다. 
score = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        num = graph[y][x] 
        for i in range(4):
            ny,nx = y+step[i][0],x + step[i][1]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] in prefer[num]:
                    cnt += 1
        if cnt == 0:
            score += 0
        elif cnt == 1:
            score += 1
        elif cnt == 2:
            score += 10
        elif cnt == 3:
            score += 100
        else:
            score += 1000
print(score)

