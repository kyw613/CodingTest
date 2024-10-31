S = input().strip()
T = input().strip()
type_same = False
while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]
    if S == T:
        type_same = True
        break

if type_same:
    print(1)
else:
    print(0)