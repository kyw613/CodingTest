def solution(book_time):
    #퇴실 시간을 기준으로 10분 청소
    # book_time이 주어질때 필요한 최소 객실 개수는?
    # 최대 겹치는걸 찾는거잖아..
    sort_book = (sorted(book_time,key=lambda x:(x[0],x[1])))
    # 시작시간과 끝나는 시간을 비교하면서 시작시간이 끝나는 시간보다 크면 끝나는 시간 없애는 형식으로
    # 이때 끝나는 시간은 +10 한상태로 저장
    # 정렬은 시작 - 끝으로
    save = []
    max_val = 0  
    for s,e in sort_book:
        e_t,e_m = map(int,e.split(":"))
        e_t += (e_m + 10) // 60
        e_m = (e_m + 10) % 60
        e = str(e_t) + ":" + str(e_m)
        if not save:
            prev = s
            save.append(e)
            max_val = max(max_val,len(save)) 
            continue
        save.append(e)
        prev = s
        prev_t,prev_m = map(int,prev.split(":"))
        for s in save:
            s_t,s_m = map(int,s.split(":"))
            if s_t < prev_t or (s_t == prev_t and s_m <= prev_m):
                save.remove(s)
        max_val = max(max_val,len(save)) 
    return max_val
        
            
            
        