import sys
input = sys.stdin.readline
N = int(input())
clain = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

if max(clain) < max(weight):
    print("-1")
else:
    clain.sort(reverse=True)
    weight.sort(reverse=True)
    result = 0
    while weight:
        result += 1
        c_idx = 0
        w_idx = 0
        while c_idx < len(clain) and w_idx < len(weight):
            if clain[c_idx] >= weight[w_idx]:
                weight.pop(w_idx)
                c_idx += 1
            else:
                w_idx += 1
    print(result)