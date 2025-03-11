N = int(input())
N_arr = list(map(int,input().split()))

M = int(input())
M_arr = list(map(int,input().split()))

N_dict = {}
for a in N_arr:
    N_dict[a] = 1


for m in M_arr:
    if m in N_dict:
        print("1")
    else:
        print("0")

    