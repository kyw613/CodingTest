import sys
input = sys.stdin.read  # sys.stdin.read()를 사용하여 빠르게 입력받기

name_dict = {}
total = 0

# 모든 입력을 한 번에 받아서 처리
data = input().strip().splitlines()

for tmp in data:
    if tmp not in name_dict:
        name_dict[tmp] = 1
    else:
        name_dict[tmp] += 1
    total += 1

for k, v in sorted(name_dict.items()):
    print(f"{k} {v / total * 100:.4f}")
