N,M,P = map(int,input().split())
if N == 0:
    print("1")
else:
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    cnt = 1
    ty = False
    if M <= arr[-1] and N == P:
        ty = True
        print("-1")
    else:
        for a in arr:
            if a <= M:
                ty = True
                print(cnt)
                break
            else:
                cnt += 1
    if ty == False:
        print(cnt)
