#M이상 N이하 소수 구하기
M , N = map(int,input().split())
if M == 1:
    M += 1
#소수인지 확인
#맞다면 print("i")후 break
for i in range(M,N+1):
    flag = True
    for k in range(2,int(i**0.5)+1):
        if i % k == 0:
            flag = False
            break
    if flag:
        print(i)

        
        