data = str(input().rstrip())
dic = {}
cnt = 0
for i in range(1,len(data)+1): # 길이
    for j in range(0,len(data)-i+1):
        if not data[j:j+i] in dic: # 없으면
            dic[data[j:j+i]] = True
            cnt += 1
print(cnt)

