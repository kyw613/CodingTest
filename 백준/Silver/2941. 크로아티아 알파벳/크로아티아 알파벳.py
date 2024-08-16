Data = input()
cnt = len(Data)
count = 0

count += Data.count('c=')
count += Data.count('c-')
count += Data.count('d-')
count += Data.count('s=')
count += Data.count('dz=') 
count += Data.count('z=')
count += Data.count('lj')
count += Data.count('nj')

print(cnt-count)