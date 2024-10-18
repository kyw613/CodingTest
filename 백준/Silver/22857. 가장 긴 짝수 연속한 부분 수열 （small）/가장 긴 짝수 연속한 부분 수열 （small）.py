N, K = map(int,input().split()) #N은 개수 K는 뺴는거 개수
S = list(map(int, input().split()))

#홀수가 k개 이상 나오면 길이 저장후 빼주기!
max_val = -1
start = 0
cnt_1 = 0
cnt_2 = 0
for e in range(N):
    if not S[e] %2:#짝수면
        cnt_2 += 1
    else:
        cnt_1 += 1
    if cnt_1 >= K:#K보다 큰경우
        max_val = max(max_val,cnt_2)
        while cnt_1 > K:
            if not S[start] % 2:
                cnt_2 -=1
            else:
                cnt_1 -=1
            start += 1
    max_val = max(max_val,cnt_2)
    
print(max_val)
        

