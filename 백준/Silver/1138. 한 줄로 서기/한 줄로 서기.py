#사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다
N = int(input())
numbers = list(map(int,input().split()))
#키랑 위치를 고려해야함
#N명의 사람 키는 1~N
#키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있나 N<10임
# 작은거부터 넣으면 되네? 1의자리 특정됨
graph = [0] * N

for i,number in enumerate(numbers): # i+1부터
    count_0 = 0
    if i ==0:
        graph[number] = i+1
    for t,k in enumerate(graph):
        if i==0:
            break
        if k == 0:
            count_0 += 1
            if count_0 == number+1:
                graph[t] = i+1
                break

print(" ".join(map(str, graph)))

    



