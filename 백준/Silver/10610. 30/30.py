#30의배수? 뒤에가 0 이고 30 60 210 240 270 더하면 3의 배수
from collections import Counter
data = str(input())
count = Counter(data)
count = sorted(count.items())
sum = 0
result = ""
type_none = False
if not '0'== count[0][0]:
    print("-1")
    type_none = True
else:
    for i in range(len(count)):
        sum += int(count[i][0]) * int(count[i][1])
    if sum % 3:
        print("-1")
        type_none = True
if not type_none:
    for k in range(len(count)-1,-1,-1):
        result += count[k][0] * int(count[k][1])
    print(result)
