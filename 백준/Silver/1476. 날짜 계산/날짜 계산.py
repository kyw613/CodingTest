#15,28,19
E, S, M = map(int,input().split())
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
e, s, m = 1, 1, 1
cnt = 1
while True:
    if e == E and s == S and m == M:
        break
    else:
        cnt += 1
        e = (e+1) % 15
        s = (s+1) % 28
        m = (m+1) % 19
print(cnt)