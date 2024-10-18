T = int(input())
for _ in range(T):
    N = int(input())
    A = []
    for _ in range(N):
        A.append(str(input()))
    A.sort()
    Ty = False
    for i in range(N-1):
        leng = len(A[i])
        if str(A[i+1]) == (str(A[i])+str(A[i+1][leng:])):
            print("NO")
            Ty = True
            break
    if not Ty:
        print("YES")
        
