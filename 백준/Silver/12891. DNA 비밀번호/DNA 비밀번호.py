N,M = map(int,input().split())
W = input().rstrip()
#
a,c,g,t = map(int,input().split())
dna_dict = {"A":0,"C":0,"G":0,"T":0}
cnt = 0

for i in range(M):
    dna_dict[W[i]] += 1
if dna_dict["A"] >= a and dna_dict["C"] >= c and dna_dict["G"] >= g and dna_dict["T"] >= t:
    cnt += 1 

for i in range(1,N-M+1):
    dna_dict[W[i-1]] -= 1
    dna_dict[W[i+M-1]] += 1
    if dna_dict["A"] >= a and dna_dict["C"] >= c and dna_dict["G"] >= g and dna_dict["T"] >= t:
        cnt += 1 

print(cnt)


