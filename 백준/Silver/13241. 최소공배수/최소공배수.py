A,B = map(int,input().split())
comp = 0
while True:
    comp += A
    if comp % B == 0:
        print(comp)
        break
    

