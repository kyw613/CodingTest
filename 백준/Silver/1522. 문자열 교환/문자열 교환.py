S = str(input())
cnt_a = S.count("a")
leng = len(S)
S = S * 2
cnt_dict = {}
cnt_dict["a"] = S[:cnt_a].count("a")
cnt_dict["b"] = S[:cnt_a].count("b")
min_cnt_b = cnt_dict["b"]

for i in range(1,leng):
    #최소 b의 개수 구하기
    if S[i-1] == "a":
        cnt_dict["a"] -=1
    else:
        cnt_dict["b"] -=1

    if S[i+cnt_a-1] == "a":
        cnt_dict["a"] += 1
    else:
        cnt_dict["b"] += 1
    min_cnt_b = min(min_cnt_b,cnt_dict["b"])
print(min_cnt_b)