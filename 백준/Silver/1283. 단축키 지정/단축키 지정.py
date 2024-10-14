import sys

N = int(input())
comp = {}  # 단축키로 사용된 글자들을 저장

for _ in range(N):
    option = input().split() # 공백 기준으로 나눔
    found = False

    # 첫 번째로 각 단어의 첫 글자를 단축키로 지정할 수 있는지 확인
    for i in range(len(option)):
        if option[i][0].lower() not in comp:
            comp[option[i][0].lower()] = True
            option[i] = f'[{option[i][0]}]{option[i][1:]}'  
            found = True
            break

    # 첫글자 지정 못한경우 나머지 글자 중에서 가능한 것을 단축키로 지정
    if not found:
        for i in range(len(option)):
            for j in range(len(option[i])):
                if option[i][j].lower() not in comp:
                    comp[option[i][j].lower()] = True
                    option[i] = f'{option[i][:j]}[{option[i][j]}]{option[i][j+1:]}'
                    found = True
                    break
            if found:
                break

    #단축키 없으면 그냥 출력
    print(' '.join(option))
