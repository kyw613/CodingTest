import sys
input = sys.stdin.readline

n = int(input().strip())  # 입력값에서 공백을 제거하기 위해 strip() 사용
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print("1")
else:
    print("0")
