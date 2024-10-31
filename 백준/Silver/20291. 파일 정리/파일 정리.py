N = int(input())
ext_dict = {}
for _ in range(N):
    name,ext = map(str,input().split("."))
    if not ext in ext_dict:
        ext_dict[ext] = 1
    else:
        ext_dict[ext] += 1

for e,c in sorted(ext_dict.items()):
    print(e,c)