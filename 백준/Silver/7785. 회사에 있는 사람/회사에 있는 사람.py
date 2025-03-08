N = int(input())
name_dict = {}
for tc in range(N):
    name, ty = map(str,input().split())
    if ty == "enter":
        name_dict[name] = 1
    elif ty == "leave":
        del(name_dict[name])
arr = sorted(name_dict.keys(),reverse = True)
for a in arr:
    print(a)