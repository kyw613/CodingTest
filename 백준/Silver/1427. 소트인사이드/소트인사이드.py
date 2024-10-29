import sys
input = sys.stdin.readline

data = str(input())
s = []
for i in data:
    s.append((i))

s = sorted(s,reverse = True)

w = "".join(s)
print(w)
