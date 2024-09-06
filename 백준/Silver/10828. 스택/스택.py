import sys
input = sys.stdin.read

commands = input().splitlines()  # 전체 입력을 한 번에 읽고 각 줄을 분리
n = int(commands[0])  # 첫 번째 줄은 명령의 수
stack = []

# 각 명령을 처리
for i in range(1, n + 1):
    command = commands[i].split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")
