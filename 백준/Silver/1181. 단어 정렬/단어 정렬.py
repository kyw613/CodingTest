#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#단, 중복된 단어는 하나만 남기고 제거해야 한다.
N = int(input())

w_i = {}
for _ in range(N):
    a = str(input())
    if not a in w_i:
        w_i[a] = True


w_i = sorted(w_i.keys(),key=lambda x:(len(x),x))

for i in range(len(w_i)):
    print(w_i[i])