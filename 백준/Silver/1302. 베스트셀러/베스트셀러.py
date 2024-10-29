N = int(input())
name_dict = {}
for _ in range(N):
    a = input()
    if not a in name_dict:
        name_dict[a] = 1
    else:
        name_dict[a] += 1
#첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
#만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
name_dict = sorted(name_dict.items(),key=lambda x:(-x[1],x[0]))
print(name_dict[0][0])