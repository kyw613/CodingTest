N = int(input())
price = list(map(int, input().split()))
price.sort()

# 이분탐색 파라메트릭 서치 사용
total = int(input())
start = 0
end = price[-1]

if sum(price) <= total:
    print(max(price))
else:
    while start <= end:
        mid = (start + end) // 2
        comp_sum = 0
        
        # mid보다 작은 값들은 그대로 더하고, 큰 값들은 mid로 더함
        for i in price:
            if i > mid:
                comp_sum += mid
            else:
                comp_sum += i

        # 예산을 초과
        if comp_sum > total:
            end = mid - 1
        # 예산보다 작음
        else:
            start = mid + 1

    print(end)
