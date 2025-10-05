
import sys
from collections import deque

input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution():
    
    def bfs(x, y):
        visited = [[-1]*w for _ in range(h)]
        visited[x][y] = 0
        queue = deque([(x, y, 0)])
        while queue:
            r, c, cnt = queue.popleft()
            for dr, dc in delta:
                nr, nc = r+dr, c+dc
                if h > nr >= 0 and w > nc >= 0:
                    if visited[nr][nc] == -1:
                        if board[nr][nc] == '#':
                            visited[nr][nc] = cnt+1
                            queue.append((nr, nc, cnt+1))
                        elif board[nr][nc] != '*':
                            visited[nr][nc] = cnt
                            queue.appendleft((nr, nc, cnt))
                        else:
                            visited[nr][nc] = -2
        return visited

    T = int(input())
    for t in range(T):
        h, w = map(int, input().split())
        w += 2
        board = [['.']*w]+[['.']+[*input().rstrip()]+['.'] for _ in range(h)]+[['.']*w]
        h += 2
        P = []
        for r in range(1, h-1):
            for c in range(1, w-1):
                if board[r][c] == '$':
                    P.append((r, c))
        visited1 = bfs(0, 0)
        visited2 = bfs(P[0][0], P[0][1])
        visited3 = bfs(P[1][0], P[1][1])
        res = h*w
        for r in range(h):
            for c in range(w):
                if visited1[r][c] >= 0 and visited2[r][c] >= 0 and visited3[r][c] >= 0:
                    door = visited1[r][c]+visited2[r][c]+visited3[r][c]
                    if board[r][c] == '#':
                        door -= 2
                    if door < res:
                        res = door
        print(res)

solution()