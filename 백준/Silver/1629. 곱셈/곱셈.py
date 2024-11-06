def power(a,b,c):
    if b == 0:
        return 1
    x = power(a,b//2,c)

    if b % 2:
        return (x*x*a)%c
    else:
        return (x*x)%c

A, B, C = map(int, input().split())
ans = power(A,B,C)
print(ans)