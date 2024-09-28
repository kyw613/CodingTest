N, M, K = map(int, input().split())
fireballs = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

# 방향 설정 
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


for step in range(K):
    
    # 파이어볼 이동 후 저장(좌표마다 저장 예정)
    new_positions = [[[] for _ in range(N)] for _ in range(N)]
    
    # 파이어볼 이동
    for r, c, m, s, d in fireballs:
        dr, dc = directions[d]
        nr = (r + dr * s) % N  
        nc = (c + dc * s) % N
        #nr = (nr + N) % N  # 음수 좌표 처리
        #nc = (nc + N) % N  # 음수 좌표 처리
        new_positions[nr][nc].append([m, s, d])

    # 새 파이어볼 리스트
    fireballs = []
    
    # 알고리즘 구현
    for r in range(N):
        for c in range(N):
            if len(new_positions[r][c]) == 1:  
                fireballs.append([r, c] + new_positions[r][c][0])
            elif len(new_positions[r][c]) > 1:  # 파이어볼이 2개 이상
                total_mass = sum(f[0] for f in new_positions[r][c])
                total_speed = sum(f[1] for f in new_positions[r][c])
                count = len(new_positions[r][c])
                new_mass = total_mass // 5
                if new_mass > 0:  # 질량이 0인 경우 생성x
                    new_speed = total_speed // count
                    all_even = all(f[2] % 2 == 0 for f in new_positions[r][c])
                    all_odd = all(f[2] % 2 != 0 for f in new_positions[r][c])
                    if all_even or all_odd:  # 모두 짝수거나 모두 홀수인 경우
                        new_dirs = [0, 2, 4, 6]
                    else:
                        new_dirs = [1, 3, 5, 7]
                    for d in new_dirs:
                        fireballs.append([r, c, new_mass, new_speed, d])
    
print(sum(f[2] for f in fireballs))
