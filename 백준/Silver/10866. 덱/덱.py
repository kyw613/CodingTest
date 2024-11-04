from collections import deque
import sys
input = sys.stdin.readline
A = deque()
N = int(input())
for i in range(N):
    string = input().split()
    if len(string) >= 2:
        if string[0] == "push_front":
            A.insert(0,string[1])
        elif string[0] == "push_back":
            A.append(string[1])
    else:
        if string[0] == "pop_front":
            if not A:
                print("-1")
            else:
                print(A.popleft())
        elif string[0] == "pop_back":
            if not A:
                print("-1")
            else:
                print(A.pop())
        elif string[0] == "size":
            print(len(A))
        elif string[0] == "empty":
            if not A:
                print("1")
            else:
                print("0")      
        elif string[0] == "front":
            if not A:
                print("-1")
            else:
                print(A[0])
        elif string[0] == "back":
            if not A:
                print("-1")
            else:
                print(A[-1])
                
        