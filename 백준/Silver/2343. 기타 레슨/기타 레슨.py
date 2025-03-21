

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

low = max(lectures)
high = sum(lectures)
answer = high

while low <= high:
    mid = (low + high) // 2
    
    count = 1
    total = 0
    for length in lectures:
        if total + length > mid:
            count += 1
            total = length
        else:
            total += length


    if count <= M:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)

