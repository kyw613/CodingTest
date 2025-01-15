def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
        
def solution(n, k):
    # 일단 소수라 뒤에 0이 들어가면 안됨..
    # 1. 방법1 그냥 0으로 나눈것을 확인해보기...
    # 먼저 k진수로 바꾸기 부터 해야한다.
    start = n
    k_num = ""
    result = 0
    while True:
        if start < k:
            k_num += str((start % k))
            break
        k_num += str(start % k)
        start = start // k
    k_num = k_num[::-1]
    words = list(map(str,k_num.split("0")))
    for k in words:
        if k == "":
            continue
        if is_prime(int(k)):
            result += 1
    return result

            
            