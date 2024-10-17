T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    
    max_val = -1
    min_val = 1000000
    idx_list = {}

    for i in range(len(W)):
        if W[i] not in idx_list:
            idx_list[W[i]] = []
        idx_list[W[i]].append(i)  # 해당 문자의 위치 저장

    for key, idxs in idx_list.items():
        # 문자가 K번 이상 등장할 경우
        if len(idxs) >= K:
            for i in range(len(idxs) - K + 1):
                current_len = idxs[i + K - 1] - idxs[i] + 1
                max_val = max(max_val, current_len)
                min_val = min(min_val, current_len)

    if max_val == -1:
        print(-1)
    else:
        print(min_val, max_val)
