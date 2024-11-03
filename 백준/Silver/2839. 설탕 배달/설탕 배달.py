#Nkg 3kg,5kg봉지로 최소한의 주머니 사용. 못만들면 -1
N = int(input())

end = N // 5
if end == 0:
    if N == 3:
        print("1")
    elif N == 0:
        print("0")
    else:
        print("-1")
else:
    flag = True
    for i in range(end,-1,-1):
        total = N
        total -= (5 * i)
        if total % 3 == 0:
            print(i + (total //3))
            flag = False
            break
    if flag:
        print("-1")
