X,Y = map(int,input().split())
init_Z = (Y*100)//X
cnt = 0
if init_Z >= 99:
    print("-1")
else:
    answer = -1
    start = 0
    end = X
    while start <= end:
        mid = (start+end) // 2
        if ((Y+mid)*100) // (X+mid) > init_Z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    print(answer)

        
