def check(chr1,chr2):
    cnt = 0
    for i in range(len(chr1)):
        if chr1[i] == chr2[i]:
            cnt += 1
    return cnt
# 슬라이딩 윈도우 문제!
A,B = map(str,input().split())

max_cnt = 0
cnt = 0

# 이거 많이 겹치는거로 했는데 조금 바뀌는걸로 해도 ㄱㅊ
for i in range(0,len(B)-len(A)+1):
    cnt = check(A,B[i:i+len(A)])
    max_cnt = max(max_cnt,cnt)
print(len(A)-max_cnt)
