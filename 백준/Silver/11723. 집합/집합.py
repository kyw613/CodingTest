import sys
input = sys.stdin.readline
N = int(input())
num = {}
for _ in range(N):
    a = input().strip()
    if " " in a:
        a,b = map(str,a.split())
        b = int(b)
    if a == "all":
        num = {i: 1 for i in range(1, 21)}
    elif a == "add":
        num[b] = 1
    elif a == "remove":
        if b in num:
            del(num[b])
    elif a == "check":
        if b in num:
            print("1")
        else:
            print("0")
    elif a == "toggle":
        if b in num:
            del(num[b])
        else:
            num[b] = 1
    elif a == "empty":
        num = {}
