def solution(files):
    #Head, Number, Tail을 구분하는게 숫자 나오기 전,숫자,그 이후란 말이지.
    # 이때 대소문자는 비교하지 않고. 숫자는 연속된 숫자로 최대 5글자!
    comp = []
    result = []
    set_idx = 0
    for file in files:
        num_ty = False
        alpha_cnt = 0
        num_cnt = 0
        for f in range(len(file)):
            if num_ty == False and file[f].isnumeric()==False:
                alpha_cnt += 1
            elif num_ty == False and file[f].isnumeric():
                num_ty = True
            if num_ty == True and file[f].isnumeric():
                num_cnt += 1
            elif num_ty== True and (file[f].isnumeric() == False or num_cnt >= 5):
                break
        comp.append((file[:alpha_cnt],file[alpha_cnt:num_cnt+alpha_cnt],file[num_cnt+alpha_cnt:],set_idx))
        set_idx += 1
    comp.sort(key=lambda x:(x[0].lower(),int(x[1]),x[3]))
    
    for h,n,t,_ in comp:
        answer = ""
        answer += h + n + t
        answer.replace(" ","")
        result.append(answer)
    return result

    
    
            
            