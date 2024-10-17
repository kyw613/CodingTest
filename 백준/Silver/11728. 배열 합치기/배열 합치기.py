N , M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B 
C.sort()
C_str = list(map(str, C))
j = " ".join(C_str)
print(j)