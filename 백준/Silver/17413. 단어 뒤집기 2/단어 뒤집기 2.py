data = input().strip()
result = ""
temp = "" # 역순바꾸기 위해
inside_tag = False

for char in data:
    if char == "<":
        inside_tag = True
        result += temp[::-1]
        temp = ""
        result += char
    elif char == ">":
        inside_tag = False
        result += char
    elif inside_tag:
        result += char
    elif char == " ":
        result += temp[::-1] + " "
        temp = ""
    else:
        temp += char
#남은단어 추가
result += temp[::-1]

print(result)
