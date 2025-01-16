# 음 먼저 
from itertools import combinations
N, M = map(int,input().split()) # N은 행수 M은 남길 치킨짐 개수
# 1. 먼저 조합을 사용해서 치킨짐 남기는 만큼 해도 되는거고..
# 어떻게 없애면 될까?
chicken = []
house = []
for i in range(N):
    li = list(map(int,input().split()))
    for t in range(len(li)):
        if li[t] == 1:
            house.append((i,t))
        elif li[t] == 2:
            chicken.append((i,t))
chs = list(combinations(chicken,M))

min_val = 10000000000
for c in range(len(chs)):
    total = 0
    for h in house:
        min_cnt = 1000000000
        for ch in chs[c]:
            min_cnt = min(min_cnt,abs(h[0]-ch[0])+abs(h[1]-ch[1]))
        total += min_cnt
    min_val = min(min_val,total)
print(min_val)

