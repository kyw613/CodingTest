vowels = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"

while True:
    type = 0
    type_1 = 0
    v_count = 0  # 모음
    c_count = 0  # 자음
    input_data = input().strip()  # 공백 제거
    if input_data == "end":
        break
    for i in input_data:
        if i in vowels:
            type_1 += 1
    
    # 모음이 하나도 없는 경우 처리
    if type_1 == 0:
        print(f"<{input_data}> is not acceptable.")
        type = 1

    # 모음과 자음이 연속으로 3개 이상 있는지 체크
    for i in input_data:
        if type == 0:
            if i in vowels:  # 모음인 경우
                v_count += 1
                c_count = 0  # 자음 카운트 초기화
            elif i in consonant:  # 자음인 경우
                c_count += 1
                v_count = 0  # 모음 카운트 초기화
            if v_count >= 3 or c_count >= 3:
                print(f"<{input_data}> is not acceptable.")
                type = 1
                break

    # 같은 문자가 연속으로 2번 이상 나타나는 경우(ee, oo는 예외)
    for i in range(1, len(input_data)):  
        if type == 0:
            if input_data[i - 1] == input_data[i]:
                if input_data[i] != "e" and input_data[i] != "o":
                    print(f"<{input_data}> is not acceptable.")
                    type = 1
                    break

    if type == 0:
        print(f"<{input_data}> is acceptable.")
