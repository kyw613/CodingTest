T = int(input())
for _ in range(T):
    A = int(input()) - 1 # idx로 변환
    Array = [1,1,1,2,2]
    if A <= 4:
        print(Array[A])
    else:
        for i in range(4,A):
            tot = Array[i] + Array[i-4]     
            Array.append(tot)
        print(Array[-1])