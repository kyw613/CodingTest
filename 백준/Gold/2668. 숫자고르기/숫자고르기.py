N = int(input())
up = []
down = []
for i in range(1,N+1):
    a = int(input())
    up.append(i) #   (번호)
    down.append(a) # 숫자

while True:
    if set(up) == set(down):
        break
    for i in range(len(up)-1,-1,-1):
        if not up[i] in down:
            up.pop(i)
            down.pop(i) 

# 개수 출력후 작은순서로 출력!
s = set(down)
if 0 in s:
    s.remove(0)
print(len(s))

for value in sorted(s):
    print(value)

            
