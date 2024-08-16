data = input()
data = data.lower()  
array = [0] * 26 
comp = "abcdefghijklmnopqrstuvwxyz"

for i in data:
    if i in comp:  
        index = comp.index(i)  
        array[index] += 1  

max_freq = max(array)
if array.count(max_freq) > 1:
    print("?")
else:
    max_index = array.index(max_freq)
    print(comp[max_index].upper())
