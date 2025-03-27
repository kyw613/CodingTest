W,H,N,M = map(int,input().split())
a,b=0,0
N += 1
M += 1
if W//N == W/N:
    a = W//N
else:
    a = (W//N)+1
if H//M == H/M:
    b = H//M
else:
    b = (H//M)+1
print(a*b)  