def solution(board, moves):
    stack = []
    n = len(board)
    graph = []
    answer = 0
    for i in range(n):
        graph.append([board[k][i] for k in range(n) if board[k][i] != 0 ] )
    for m in moves:
        if not graph[m-1]:
            continue
        s = graph[m-1].pop(0)
        if not stack:
            stack.append(s)
        elif stack[-1] == s:
            stack.pop()
            answer += 2
        else:
            stack.append(s)
    return answer
        
        


    