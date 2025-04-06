N,M,K = map(int,input().split())

fireball_list = []
step = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    fireball_list.append((r,c,m,s,d))

for i in range(K):
    Graph = [[[] for _ in range(N)] for _ in range(N)] # 0-idx # 여기에 저장해야징
    # 각자의 방향 속력으로 이동
    for f in fireball_list:
        r,c,m,s,d = f[0],f[1],f[2],f[3],f[4]
        nr,nc  = (r + s * step[d][0] + N)%N , (c + s * step[d][1] + N )%N 
        Graph[nr][nc].append((nr,nc,m,s,d))
    fireball_list = []
    # 분할
    for y in range(N):
        for x in range(N):
            if len(Graph[y][x]) >= 2:
                cal = Graph[y][x]
                #질량 합치고 //5 , 속력 다 합친거 // 개수
                m = 0
                s = 0
                ty_1,ty_0 = False, False
                tyty = False
                for t in cal:
                    m += t[2]
                    s += t[3]
                    if t[4] % 2 == 1 and ty_0 == False: # 홀수면
                        ty_1 = True
                    elif t[4] % 2 == 0 and ty_1 == False:
                        ty_0 = True
                    else:
                        tyty = True
                m = m // 5
                s = s // len(Graph[y][x])
                if tyty == True and m!= 0: # 홀수
                    for i in range(1,8,2):
                        fireball_list.append((y,x,m,s,i))
                else:
                    if m == 0:
                        continue
                    for i in range(0,7,2):
                        fireball_list.append((y,x,m,s,i))
            elif len(Graph[y][x]) == 1:
                cal = Graph[y][x]
                for t in cal:
                    fireball_list.append((t[0],t[1],t[2],t[3],t[4]))
cnt = 0
if fireball_list:
    for t in fireball_list:
        cnt += t[2]
    print(cnt)
else:
    print(0)
    


