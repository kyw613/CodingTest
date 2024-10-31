data = input()
comp = input()
max_length = 0
dp = [0]*(len(comp)+1)

for i in range(len(data)):
    for j in range(len(comp) - 1, -1, -1):
        if comp[j] == data[i]:
            dp[j+1] = dp[j] + 1
            max_length = max(dp[j+1],max_length)
        else:
            dp[j+1] = 0
    
print(max_length)