N,K = map(int,input().split())
array = [i+1 for i in range(N)]
idx  = 0
result = []
while array:
    idx += K-1
    idx = idx % len(array)
    a = array.pop(idx)
    result.append(str(a))
print("<"+", ".join(result)+">")