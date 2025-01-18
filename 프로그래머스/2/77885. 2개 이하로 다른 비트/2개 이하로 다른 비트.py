def solution(numbers):
    result = []
    for number in numbers:
        #number를 2진수 비트로
        bit = bin(number)[2:]
        leng = bit.count("1")
        if len(bit) == leng :
            bit = "1" + "0" + "1"* (leng-1)
        else:
            for i in range(len(bit)-1,-1,-1):
                if bit[i] == "0":
                    break
            if i == len(bit) -1:
                bit = bit[:len(bit)-1] + "1"
            else:
                bit = bit[:i] + "10" + bit[i+2:]
        total = 0
        length = len(bit) -1
        for b in range(len(bit)-1,-1,-1):
            total += int(bit[b]) * (2**(length-b))
        result.append(total)
    return result
        
        