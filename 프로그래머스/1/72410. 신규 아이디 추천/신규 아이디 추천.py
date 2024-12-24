def solution(new_id):
    #아이디 알파벳 소문자 숫자 ("-","_",".") 이때 .은 처음과 끝 x 연속 x
    possible = "abcdefghijklmnopqrstuvwxyz1234567890-_."
    id = ""
    for s in new_id.lower():
        if s in possible:
            id += s
    ty = False
    result = ""
    for i in range(len(id)):
        if ty == False and id[i] == ".":
            result += id[i]
            ty = True
        elif ty == True and id[i] == ".":
            continue
        elif id[i] != ".":
            result += id[i]
            ty = False
    if result[0] == ".":
        result = result[1:]
    if not result:
        result += "a"
    if result[-1] == ".":
        result = result[:len(result)-1]
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == ".":
            result = result[:len(result)-1]
    if len(result) == 1:
        result += result[-1] * 2
    elif len(result) == 2:
        result += result[-1]
    return result
            
        