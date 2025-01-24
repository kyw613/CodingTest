def solution(n):
    array = [[0] * (i + 1) for i in range(n)]
    dz = [(1, 0), (0, 1), (-1, -1)]
    
    x, y = 0, 0 # 시작위치
    direction = 0
    num = 1
    
    for _ in range(1, n * (n + 1) // 2 + 1):
        array[x][y] = num
        num += 1
        
        nx, ny = x + dz[direction][0], y + dz[direction][1]
        # 이동 불가하면 방향전환
        if nx < 0 or ny < 0 or nx >= n or ny >= len(array[nx]) or array[nx][ny] != 0:
            direction = (direction + 1) % 3
            nx, ny = x + dz[direction][0], y + dz[direction][1]
        x, y = nx, ny
    result = []
    for row in array:
        result.extend(row)
    return result

