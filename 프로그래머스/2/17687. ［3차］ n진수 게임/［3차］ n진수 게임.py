def solution(n, t, m, p):
    # n진수로 t개 바꾸고 리스트에 넣기
    number = ""
    for k in range(t*m,-1,-1):
        start = k
        if start == 0:
            number += "0"
        while True:
            if start < n:
                if start % n < 10:
                    number += str(start % n)
                    break
                else:
                    number += str(chr((start % n) - 10 + ord("A")))
                    break
            if start % n < 10:
                number += str(start % n)
            else:
                number += str(chr((start % n) - 10 + ord("A")))
            start = start // n
    number = number[::-1]
    result = ""
    for i in range(p,len(number),m):
        result += str(number[i])
    return result[:t]
        
            
        