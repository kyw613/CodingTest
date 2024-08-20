from collections import Counter

def solution(clothes):
    # 의상 종류별로 개수를 세기
    counter = Counter([kind for name, kind in clothes])
    
    combinations = 1
    for count in counter.values():
        combinations *= (count + 1)
    
    # 아무것도 입지 않은 경우를 제외
    return combinations - 1
