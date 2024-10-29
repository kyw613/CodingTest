data = input()
name_dict = {}
for i in range(0,len(data)):
    name_dict[data[i::]] = True
name_dict = sorted(name_dict.keys())
for k in name_dict:
    print(k)
