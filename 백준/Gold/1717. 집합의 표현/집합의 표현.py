# union and find 사용하면 편할듯?
import sys

sys.setrecursionlimit(10**6)
n, m = map(int,input().split())
# dp는 자기 자신
dp = [0] * (n+1)
for i in range(n+1):
    dp[i] = i

def union_parent(dp,a,b):
    a = find_parent(dp,a)
    b = find_parent(dp,b)
    if a<b:
        dp[b] = a
    else:
        dp[a] = b
    

def find_parent(dp,x):
    if x == 0:
        return 0
    if dp[x] != x:
        dp[x] = find_parent(dp,dp[x])
    return dp[x]
    
for _ in range(m):
    t,a,b = map(int,input().split())
    if t == 0:
        union_parent(dp,a,b)
    else:
        if find_parent(dp,a) == find_parent(dp,b):
            print("YES")
        else:
            print("NO")