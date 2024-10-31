#알파벳 소문자로 이루어짐 + 3부분으로 나누어(2번 잘라) 사전상 가장 앞에 오는 말...

data = input().rstrip()
Array = []
for i in range(len(data)-2):
    for j in range(i+1,len(data)-1):
        a = data[:i+1]
        b = data[i+1:j+1]
        c = data[j+1:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        Array.append(a+b+c)

Array.sort()
print(Array[0])