def solution(n,a,b):
    # 수학적 계산으로? 
    # //2를 해서 +1하면 같은값이 되나 확인 이떄 1//1을 1로 만들어야함
    #1. 일단 a가 작은거 b가 큰거
    if a > b:
        a,b = b,a
    cnt = 1
    while True:
        if a+1 == b and a%2:
            return cnt
        if a % 2:
            a = a//2 + 1
        else:
            a =  a // 2
        if b % 2:
            b = b//2 + 1
        else:
            b = b // 2
        cnt += 1