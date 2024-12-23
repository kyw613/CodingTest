def solution(N, stages):
    answer = []
    up = [0] * (N+1)
    down = [0] * (N+1)
    comp = []
    result = []
    answer = []
    for i in stages:
        if i == N+1:
            for k in range(1,N+1):
                down[k] += 1
        else:
            for t in range(1,i+1):
                down[t] += 1
            up[i] += 1
    for a,b in zip(up[1:],down[1:]):
        if b == 0:
            comp.append(0)
        else:
            comp.append(a/b)
    for idx,value in enumerate(comp):
        result.append((idx+1,value))
    result.sort(key=lambda x:(-x[1],x[0]))
    for x,y in result:
        answer.append(x)
    return answer
        
        
        
                
                
        