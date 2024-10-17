import sys
input = sys.stdin.readline

while True:
    # 상근과 선영의 CD 개수를 입력받음
    N, M = map(int, input().split())
    
    # 종료 조건 (0 0 입력 시 종료)
    if N == 0 and M == 0:
        break
    
    # 상근이 가지고 있는 CD를 저장할 딕셔너리
    A = {}
    for _ in range(N):
        A[int(input().rstrip())] = 1  # 상근이 가진 CD를 딕셔너리에 저장

    # 선영이 가지고 있는 CD를 저장할 리스트
    B = []
    for _ in range(M):
        B.append(int(input().rstrip()))  # 선영이 가진 CD를 리스트에 저장

    # 상근과 선영이 동시에 가지고 있는 CD 개수 계산
    cnt = 0
    for x in B:
        if x in A:  # 상근의 CD 리스트에 있으면 카운트
            cnt += 1

    # 결과 출력
    print(cnt)
