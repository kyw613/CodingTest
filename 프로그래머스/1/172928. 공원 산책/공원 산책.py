def solution(park, routes):
    H = len(park)
    W = len(park[0])
    #1. 시작위치찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x, y = i, j

    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    for route in routes:
        direction, distance = route.split()
        distance = int(distance)

        dx, dy = directions[direction]
        nx, ny = x, y
        valid_move = True
        
        for _ in range(distance):
            nx += dx
            ny += dy
            if not (0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':
                valid_move = False
                break
        if valid_move:
            x, y = nx, ny
    return [x, y]
