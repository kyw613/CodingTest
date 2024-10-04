n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

result = [0,0,0]

def check(x, y, n):
    comp = graph[x][y]
    for i in range(n):
        for j in range(n):
            if comp != graph[x+i][y+j]:
                return False
    return True


def count(x ,y ,n):
    standard = graph[x][y]

    if check(x,y,n):
        result[standard + 1] += 1
        return
    
    nn = n //3
    for a in range(3):
        for b in range(3):
            count(x+nn*a,y+nn*b,nn)

count(0,0,n)

for i in range(3):
    print(result[i])
        
