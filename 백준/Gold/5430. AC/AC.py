import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    func = input()
    n = int(input())
    A = input().strip()[1:-1]
    if A:
        A = list(map(int, A.split(",")))
    else:
        A = []
    reverse_flag = False
    error_flag = False
    for i in func:
        if i == "R":
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        elif i == "D":
            if n == 0:
                print("error")
                error_flag = True
                break
            if not reverse_flag:
                A.pop(0)
            else:
                A.pop()
            n -= 1
    if reverse_flag:
        A.reverse()
    if not error_flag:
        print(f"[{','.join(map(str, A))}]")