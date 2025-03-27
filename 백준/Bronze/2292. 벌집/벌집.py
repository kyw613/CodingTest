N = int(input())
idx = 0
cnt = 0
total = 1
if N ==1 :
    print("1")
else:
    while True:
        idx += 1
        if total < N <= total + 6*idx:
            print(idx+1)
            break
        else:
            total = total + 6*idx
    


