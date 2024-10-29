N, M = map(int,input().split())

see_dict = {}
listen_dict = {}
name = []
for _ in range(N):
    input_data = str(input())
    see_dict[input_data] = True
for _ in range(M):
    input_data = str(input())
    listen_dict[input_data] = True
cnt = 0
for i in see_dict.keys():
    if i in listen_dict:
        cnt += 1
        name.append(i)

print(cnt)
name.sort()
for n in name:
    print(n)