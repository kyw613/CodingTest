from collections import deque
F,S,G,U,D = map(int,input().split())
visit  = [True] * (F+1)
q = deque([(0,S)])
step = [U,-D]
visit[S]= False
ty  =False
while q:
    idx,s = q.popleft()
    if s == G:
        print(idx)
        ty = True
        break
    for i in range(2):
        ns = s + step[i]
        if 1 <= ns < F+1 and visit[ns] == True:
            visit[ns] = False
            q.append((idx+1,ns))
if ty ==False:
    print("use the stairs")

    
