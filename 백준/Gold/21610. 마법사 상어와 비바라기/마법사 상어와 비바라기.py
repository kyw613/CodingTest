N,M = map(int,input().split()) # N= 격자수 M = 이동수
A = [] # 0-idx이므로 idx 변환 필요
move = [] # 1-idx이므로 변환 넣기
for _ in range(N):
    A.append(list(map(int,input().split())))

for _ in range(M):
    move.append(list(map(int,input().split())))
#비바라기 시전시 (N-1,0),(N-2,0),(N-1,1),(N-2,1) 생성
step = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] #x,y로 저장
check = [(-1,-1),(1,-1),(1,1),(-1,1)]
guroom_list = [(N-1,0),(N-2,0),(N-1,1),(N-2,1)]
for k in range(M):
    move_guroom_list = []
    for g in guroom_list:
        y,x = g[0],g[1]
        d,s = move[k][0],move[k][1]
        ny = ((y + s*step[d-1][1])+N)%N
        nx = ((x + s*step[d-1][0])+N)%N
        A[ny][nx] += 1
        move_guroom_list.append((ny,nx))
        #물의양 1 증가
        #move_guroom_list에 저장
    for m in move_guroom_list:
        y,x = m[0],m[1] # 대각선 확인후 물이 있는 바구니 수만큼 +1
        for i in range(4):
            ny,nx = y+check[i][0], x+check[i][1]
            if 0 <= ny < N and 0 <= nx < N:
                if A[ny][nx] > 0:
                    A[y][x] += 1
    guroom_list = []
    for y in range(N):
        for x in range(N):
            if (y,x) not in move_guroom_list:
                if A[y][x] >= 2:
                    A[y][x] -= 2
                    guroom_list.append((y,x))
cnt = 0
for i in range(N):
    cnt += sum(A[i])
print(cnt)
    # 바구니에 저장된 물양이 2 이상이면 구름이 생기고 2가 줄어듬. -> 이거 guroom_list초기화후 넣어야겠지?
    # 이때 확인 조건에 move_guroom_list에 없어야함
# 마지막에 이동후 전체의 합 구하기.
    
    




