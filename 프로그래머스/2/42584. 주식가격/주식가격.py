def solution(prices):
    # 일단 개 쉽게는 이렇게 할수 있지
    result = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        result.append(cnt)
    return result