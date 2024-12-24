from collections import deque

def bfs(x, y, array, answer):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visit = [[False] * 3 for _ in range(4)]
    queue = deque([(0, x, y)])  # (cnt, x, y)
    visit[y][x] = True

    while queue:
        cnt, x, y = queue.popleft()
        if array[y][x] == answer:
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 4 and not visit[ny][nx]:
                queue.append((cnt + 1, nx, ny))
                visit[ny][nx] = True

def position(n, graph):
    for j in range(4):
        for i in range(3):
            if graph[j][i] == n:
                return (i, j)

def solution(numbers, hand):
    result = ""
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    now_left = (0, 3)
    now_right = (2, 3)

    for n in numbers:
        # 1,4,7은 왼손 3,6,9는 오른손
        target_pos = position(n, array)
        if n == 1 or n==4 or n==7:
            now_left = target_pos
            result += "L"
        elif n == 3 or n == 6 or n ==9:
            now_right = target_pos
            result += "R"
        else:
            left_dist = bfs(now_left[0], now_left[1], array, n)
            right_dist = bfs(now_right[0], now_right[1], array, n)

            if left_dist < right_dist:
                now_left = target_pos
                result += "L"
            elif left_dist > right_dist:
                now_right = target_pos
                result += "R"
            else:  # 거리가 같을 경우
                if hand == "right":
                    now_right = target_pos
                    result += "R"
                else:
                    now_left = target_pos
                    result += "L"

    return result
