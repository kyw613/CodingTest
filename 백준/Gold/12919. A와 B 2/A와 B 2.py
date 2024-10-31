data = input()
comp = input()

result = 0
def dfs(str_data):
    global result
    if str_data == data:
        result =  1
    if len(str_data) == 0:
        return 0
    if str_data[-1] == "A":
        dfs(str_data[:-1])
    if str_data[0] == "B":
        dfs(str_data[1:][::-1])
dfs(comp)
print(result)