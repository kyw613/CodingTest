def check(board,y,x):
    comp = board[y][x]
    if comp==0:
        return False
    for xx in range(x,x+2):
        for yy in range(y,y+2):
            if board[yy][xx] != comp:
                return False
    return True
def solution(m, n, board):
    #2x2로 붙어있으면 사라지면서 점수를 얻음
    # 음 없어지면 y,x를 저장한후 없애서 0으로 바꾸고 내려보내는걸 해야겠다.
    graph = [[0] * n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            graph[y][x] = board[y][x]
    while True:
        start = []
        type_check = False
        for y in range(m-1):
            for x in range(n-1):
                if check(graph,y,x):
                    start.append((y,x))
                    type_check = True
        if type_check==False:
            break

                    
        # graph 초기화.
        for r_y,r_x in start:
            for y in range(r_y,r_y+2):
                for x in range(r_x,r_x+2):
                    graph[y][x] = 0


        new_graph = [[0] * n for _ in range(m)]
        for y in range(m-1,-1,-1):
            for x in range(n-1,-1,-1):
                if graph[y][x] != 0:
                    new_graph[y][x] = graph[y][x]
                else:
                    idx = 1
                    while True:
                        if y-idx < 0:
                            break
                        if graph[y-idx][x] == 0:
                            idx += 1
                        else:
                            new_graph[y][x] = graph[y-idx][x]
                            graph[y-idx][x] = 0
                            break

        graph = []
        for i in range(m):
            graph.append(new_graph[i])
    cnt = 0
    for i in range(m):
        cnt += graph[i].count(0)
    return cnt
        
        
            
            
    