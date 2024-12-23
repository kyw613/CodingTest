def solution(board, h, w):
    n = len(board)
    cnt = 0
    dh,dw = [0, 1, -1, 0], [1, 0, 0, -1]
    comp = board[h][w]
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0<= nh < n and 0 <= nw < n:
            if board[nh][nw] == comp:
                cnt += 1
    return cnt