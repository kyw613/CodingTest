# 최소 1개의 모음(aeiou) 2개의 자음
# 증가하는 순서로 배열
from itertools import combinations
vow = {"a":True,"e":True,"i":True,"o":True,"u":True}
L, C = map(int,input().split()) # L: 비번자릿수 C: 알파벳 개수
A = list(map(str,input().split()))
A.sort()
comb = list(combinations(A,L))

for i in range(len(comb)):
    cnt = 0
    for j in range(L):
        if comb[i][j] in vow:
            cnt += 1
    if 1 <= cnt <= L - 2:
        print("".join(comb[i]))
            



