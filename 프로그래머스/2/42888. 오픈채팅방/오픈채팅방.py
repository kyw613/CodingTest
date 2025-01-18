def solution(record):
    #닉네임 변경 1) 채팅방 나간후 새로운 닉네임으로 2) 채팅방에서 변경
    # 변경하면 기존 채팅의 닉네임도 전부 변경
    # 중복 닉네임 허용
    # 들어오고 나가거나 닉네임을 변경한 기록이 주어지고 ㅇㅋ
    # 쉽게 해보자
    # enter, leave UID만 저장을 하고 UID의 이름을 DICT에 저장하는거야 ㅇㅋ
    name_dict = {}
    order = []
    for re in record:
        if re[:5] == "Enter":
            c,u,n = map(str,re.split())
            order.append((c,u))
            if u not in name_dict:
                name_dict[u] = n
            else:
                name_dict[u] = n
        elif re[:5] == "Leave":
            c,u = map(str,re.split())
            order.append((c,u))
        else:
            c,u,n = map(str,re.split())
            name_dict[u] = n
    result = []
    for command,uid in order:
        if command == "Enter":
            result.append((f"{name_dict[uid]}님이 들어왔습니다."))
        else:
            result.append((f"{name_dict[uid]}님이 나갔습니다."))
    return result
            