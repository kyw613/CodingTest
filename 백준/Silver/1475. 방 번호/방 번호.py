# 0부터 9까지 1세트 6을 돌려서 9로 사용 가능!
data = input()
count = {}
def custom_round(a):
    if a - int(a) < 0.5:
        return int(a)
    else:
        return int(a+1)

for i in data:
    if not i in count:
        count[i] = 1
    else:
        count[i] += 1
total = 0
if "6" in count and "9" in count:
    total = custom_round((count["6"] + count["9"]) / 2)
    count["6"] = 0
    count["9"] = 0
elif "6" in count:
    total = custom_round((count["6"]) / 2)
    count["6"] = 0
    count["9"] = 0
elif "9" in count:
    total = custom_round((count["9"]) / 2)
    count["6"] = 0
    count["9"] = 0
max_val =total
for k,v in count.items():
    if max_val < v:
        max_val = v
print(max_val)
    
