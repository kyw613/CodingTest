N = int(input())
save = []
for i in range(N):
    a,b = map(str,input().split())
    save.append((int(a),b,i))
save.sort(key=lambda x:(x[0],x[2]))
for a,b,c in save:
    print(a,b)
    