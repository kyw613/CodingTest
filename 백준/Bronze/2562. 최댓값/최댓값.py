max_val = -1
for i in range(9):
    a = int(input())
    if a > max_val:
        max_val = a
        idx = i+1
print(max_val)
print(idx)
    