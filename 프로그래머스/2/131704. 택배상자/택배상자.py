def solution(order):
    # 1~ len order까지의 수가 있는데 이걸 order에 맞게 하는거구나 ㅇㅋ 확인
    stack = []
    val = 1
    order_idx = 0
    cnt = 0
    while True:
        if stack:
            if stack[-1] == order[order_idx]:
                stack.pop()
                cnt += 1
                order_idx += 1
                continue
        if val > len(order):
            break
        if val == order[order_idx]:
            cnt += 1
            order_idx += 1
        else:
            stack.append(val)
        val += 1
    return cnt
        
            