from collections import Counter
def solution(topping):
    #각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 분배
    # 자르는 방법의 수를 반환
    total =0
    #앞과 뒤의 갯수를 센후 더하거나 빼주기.
    front_dict = {}
    len_front = 0
    back_dict =  Counter(topping)
    for i in topping:
        if i not in front_dict:
            len_front += 1
            front_dict[i] = 1
        back_dict[i] -= 1
        if back_dict[i] == 0:
            del back_dict[i]
        if len_front == len(back_dict):
            total += 1
    return total
            