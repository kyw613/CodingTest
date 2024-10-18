n,c = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()
start = 1 # 길이!!
end = array[-1] - array[0] # 길이
result = 0
while start <= end:
    init = array[0]
    cnt = 1
    mid = (start + end) // 2 # 길이가 mid!
    #mid로 다 만족하는지 확인
    for i in array:
        if  init + mid <= i:
            init = i
            cnt += 1
    if cnt >= c:
        start = mid +1
        result = mid
    elif cnt < c:
        end = mid -1 
print(result)

