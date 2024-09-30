N, M = map(int, input().split())

girlgroups = {} # 멤버-> 그룹
member_to_group = {} # 그룹 -> 멤버

for i in range(N):
    group = input()
    member_numbers = int(input())
    members = []
    for _ in range(member_numbers):
        name = input()
        members.append(name)
        member_to_group[name] = group
    members.sort()
    girlgroups[group] = members


for _ in range(M):
    name_input = input()
    num_input = int(input())

    if num_input == 0:
        for member in girlgroups[name_input]:
            print(member)
    else:
        print(member_to_group[name_input])
