num = {"Y":1,"F":2,"O":3} 
N,T = map(str,input().split())
N = int(N)
arr = []
for _ in range(N):
    a = str(input())
    arr.append(a)
leng = len(set(arr))
print(leng//num[T])
