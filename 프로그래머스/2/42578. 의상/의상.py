def solution(clothes):
    # 일부가 겹처도 다른 의상을 추가로 더 착용한경우... -> 이거 부분집합
    # 먼저 카테고리로 갯수센후 각각에 +1 해서 곱한후  전체에서 -1 해주기.
    cnt_dict = {}
    for name,catalog in clothes:
        if catalog not in cnt_dict:
            cnt_dict[catalog] = 1
        else:
            cnt_dict[catalog] += 1
    total = 1
    for i in cnt_dict.values():
        total *= i+1
    return total - 1