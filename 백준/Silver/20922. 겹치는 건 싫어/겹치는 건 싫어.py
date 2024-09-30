N, K = map(int, input().split())
numbers = list(map(int, input().split()))

number_dict = {}
start = 0
max_value = 0

for end in range(N):
    number = numbers[end]
    
    # 숫자의 등장 횟수를 증가
    if number in number_dict:
        number_dict[number] += 1
    else:
        number_dict[number] = 1

    # 만약 숫자가 K번 이상 등장하면 start 포인터를 이동시켜 윈도우를 줄임
    while number_dict[number] > K:
        number_dict[numbers[start]] -= 1
        if number_dict[numbers[start]] == 0:
            del number_dict[numbers[start]]
        start += 1
    
    # 현재 윈도우의 길이를 계산하고 최대 길이로 업데이트
    max_value = max(max_value, end - start + 1)

print(max_value)
