def solution(n):
    #일단 가장 쉬운 ㅂㅅ같은 풀이
    cnt_1 = bin(n)[2:].count("1")
    while True:
        n += 1
        if bin(n)[2:].count("1") == cnt_1:
            return n
        