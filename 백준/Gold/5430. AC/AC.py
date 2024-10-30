import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    func = input().strip()
    n = int(input())
    A = input().strip()[1:-1]
    
    # 빈 문자열일 경우 빈 리스트로 처리
    if A:
        A = list(map(int, A.split(",")))
    else:
        A = []
        
    reverse_flag = False
    error_flag = False

    for i in func:
        if i == "R":
            reverse_flag = not reverse_flag
        elif i == "D":
            if not A:  # A가 비어 있는 경우
                print("error")
                error_flag = True
                break
            if not reverse_flag:
                A.pop(0)
            else:
                A.pop()
    
    if not error_flag:
        if reverse_flag:
            A = A[::-1]
        print(f"[{','.join(map(str, A))}]")
