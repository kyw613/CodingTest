# 1과 N사이의 수중 등차수열인것의 개수를 구하라.
N = int(input())
cnt = 0
for i in range(1,N+1):
    string = str(i)
    dif = 0
    if len(string) <= 2:
        cnt += 1
    else:
        dif = int(string[0]) - int(string[1])
        flag = True
        for k in range(1,len(string)-1):
            if dif != (int(string[k]) - int(string[k+1])):
                flag = False
        if flag:
            cnt += 1
print(cnt)
