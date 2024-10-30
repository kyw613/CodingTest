A = input().strip()
C4 = input().strip()
leng = len(C4)
stack = []

for char in A:
    stack.append(char)
    # 스택 끝부분이 C4와 일치하는지 확인
    if ''.join(stack[-leng:]) == C4:
        del stack[-leng:]  # 매칭된 부분 제거

# 결과 출력
result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
