def min_flips_to_unify(s):
    count_0 = 0  
    count_1 = 0  

    # 첫 번째 숫자에 대해 초기 카운트 설정
    if s[0] == '0':
        count_0 += 1
    else:
        count_1 += 1

    
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 += 1


    return min(count_0, count_1)


s = input().strip()

print(min_flips_to_unify(s))
