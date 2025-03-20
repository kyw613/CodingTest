import heapq
T = int(input())
for tc in range(T):
    n = int(input())
    save_dict = {}
    q_up = []
    q_down = []
    for _ in range(n):
        alpha,num = map(str,input().split())
        if alpha == "I":
            num = int(num)
            if num in save_dict:
                save_dict[num] += 1
            else:
                save_dict[num] = 1
            heapq.heappush(q_up,-num)
            heapq.heappush(q_down,num)
        else:
            if save_dict:
           # 최댓값 삭제
                if num == "1":
                    while q_up:
                        max_val = -heapq.heappop(q_up)
                        if max_val in save_dict and save_dict[max_val] > 0:
                            save_dict[max_val] -= 1
                            if save_dict[max_val] == 0:
                                del save_dict[max_val]
                            break

                # 최솟값 삭제
                else:
                    while q_down:
                        min_val = heapq.heappop(q_down)
                        if min_val in save_dict and save_dict[min_val] > 0:
                            save_dict[min_val] -= 1
                            if save_dict[min_val] == 0:
                                del save_dict[min_val]
                            break
                  
    if not save_dict:
        print("EMPTY")
    else:
        max_val = max(save_dict)
        min_val = min(save_dict)
        print(max_val, min_val)


