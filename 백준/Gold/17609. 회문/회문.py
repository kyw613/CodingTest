T = int(input())
for _ in range(T):        
    data = input()
    #data의 처음 끝 비교?
    cnt = 0 # 다른경우
    start = 0
    end = len(data)-1 # idx
    type_1 = False
    type_2 = False
    while start <=end:
        if data[start] == data[end]:
            start += 1
            end -= 1
        if data[start] != data[end]:
            cnt += 1
            # 왼쪽 문자 제거후 회문 되는지 확인
            data_l = data[:start] + data[start+1:]
            if data_l == data_l[::-1]:
                type_1 = True
                break
            data_r = data[:end] + data[end+1:]
            if data_r == data_r[::-1]:
                type_1 = True
                break
            if not type_1:
                type_2 = True
                break
    if type_2:
        print("2")
    elif type_1:
        print("1")
    else:
        print("0")

    



