def solution(storey):
    # 층이 0 이하론 갈ㄹ수 없다.
    # 0층이 가장 아래층 현재 엘리베이터는 민수가 있는 층
    # 한번단 돌한개 사용
    # 위로 가서 내려가든 아래로 가서 내려가는거 가능...
    # 즉 5이하는 아래 6이상은 위로
    
    # 먼저 어떻게 해야할까 102030 이라는 숫자가 있어.
    # str로 len을 구해서 최대 자릿수를 정하고.
    # 앞에서 부터 하는거야.
    storey = str(storey)
    total = 0
    # 뒤에서부터 시작
    idx = len(storey) - 1
    while storey:
        if idx == 0:
            if int(storey[idx]) > 5:
                total += 10 - int(storey[idx]) + 1
            else:
                total += int(storey[idx])
            break
        if int(storey[idx-1]) >= 5:
            if int(storey[idx]) >= 5:
                total += 10 - int(storey[idx])
                storey = storey[:len(storey)-1]
                storey = str(int(storey)+1)
                
            else:
                total += int(storey[idx])
                storey = storey[:len(storey)-1]
        else:
            if int(storey[idx]) > 5:
                total += 10 - int(storey[idx])
                storey = storey[:len(storey)-1]
                storey = str(int(storey)+1)
            else:
                total += int(storey[idx])
                storey = storey[:len(storey)-1]
        idx -= 1
    return total
                
                
        
        
    