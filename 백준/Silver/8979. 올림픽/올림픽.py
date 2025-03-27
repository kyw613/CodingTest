N,target = map(int,input().split())
arr = []
for _ in range(N):
    s,a,b,c = map(int,input().split())
    arr.append((a,b,c,s))
arr.sort(key=lambda x:(-x[0],-x[1],-x[2]))
comp = (-1,0,0,0)
cnt = 0
while True:
    a1,b1,c1,s1 = arr.pop()
    if comp[0] == a1 and comp[1] == b1 and comp[2] == c1:
        if s1 == target:
            print(cnt)
            break  
    else:
        cnt += 1
        comp = (a1,b1,c1,s1)
    if s1 == target:
        print(cnt)
        break



