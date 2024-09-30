T = int(input())

for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    
    max_price = 0
    result = 0
    
    # 뒤에서부터 탐색
    for i in range(N-1, -1, -1):
        if stocks[i] > max_price:
            max_price = stocks[i]
        else:
            result += max_price - stocks[i]  # 최고가에서 현재 주식 가격을 뺀 차익 누적
    
    print(result)
