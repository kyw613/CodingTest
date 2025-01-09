def solution(str1, str2):
    #자카트 유사도..두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값...
    # 교집합이 공집합이면 1로 정의!
    # 대문자 소문자는 무시! 2개씩 하기.
    str1_dict = {}
    for i in range(len(str1)-1):
        a = str1[i:i+2].lower()
        if not a.isalpha():
            continue
        if a not in str1_dict:
            str1_dict[a] = 1
        else:
            str1_dict[a] += 1
    str2_dict = {}
    for i in range(len(str2)-1):
            a = str2[i:i+2].lower()
            if not a.isalpha():
                continue
            if a not in str2_dict:
                str2_dict[a] = 1
            else:
                str2_dict[a] += 1
    # 교집합과 합집합을 구하기..
    intersection = 0
    plus_set = 0
    for n,v in str1_dict.items():
        if n in str2_dict:
            intersection += min(v,str2_dict[n])
            str2_dict[n] = max(v,str2_dict[n])
        else:
            str2_dict[n] = v
    for _,val in str2_dict.items():
        plus_set += val
    if intersection == 0 and plus_set == 0:
        return 65536
    return ((intersection/plus_set ) * 65536) // 1
    