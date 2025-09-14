import sys
input = sys.stdin.readline

MOD = 1000000

def fib(n):
    # (F_{n-1}, F_n) 반환, 단 n >= 2
    if n == 1:
        return (0, 1)
    if n == 2:
        return (1, 1)  # (F_1, F_2)

    fm1, fm = fib(n // 2)   # (F_{m-1}, F_m), m = n//2

    # 공식 적용
    f2m   = (fm*fm + 2*fm*fm1) % MOD          # F_{2m}
    f2m_1 = (fm*fm + fm1*fm1) % MOD           # F_{2m-1}

    if n % 2 == 0:  # n = 2m
        return (f2m_1, f2m)
    else:           # n = 2m+1
        return (f2m, (f2m + f2m_1) % MOD)


n = int(input())
print(fib(n)[1] % MOD)  # F_n
