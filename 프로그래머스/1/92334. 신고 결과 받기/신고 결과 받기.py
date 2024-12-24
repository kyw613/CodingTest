def solution(id_list, report, k):
    order = {name:i for i, name in enumerate(id_list)}
    result = [0] * len(id_list)
    #1. report 중복처리
    report_set = set(report)
    bull = {name:0 for i, name in enumerate(id_list)}
    for a in report_set:
        n1,n2 = map(str,a.split())
        bull[n2] += 1
    name = []
    for t in id_list:
        if int(bull[t]) >= int(k):
            name.append(t)
    for a in report_set:
        n1,n2 = map(str,a.split())
        if n2 in name:
            s = order[n1]
            result[s] += 1
    return result
            
            
    
    
        

    
    