def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())
ans = str(factorial(N))
ans = ans[::-1]

cnt = 0
for i in ans:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)

