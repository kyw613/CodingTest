n = int(input())

people = []

for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = [] # 각 사람의 덩치 등수를 저장할 리스트

# 덩치 등수 계산
for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
    ranks.append(rank)

print(" ".join(map(str, ranks)))
