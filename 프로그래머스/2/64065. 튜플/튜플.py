def solution(s):
    # 문자열을 구분후 넣기 그냥 가장 긴거 고르면 되네
    le = len(s)
    s = s[1:le-1]
    save = (s.split("},{"))
    result = [] # 여기서 정렬
    answer = []
    for i in save:
        val = i
        leng = len(i)
        if "{" in i:
            val = i[1:]
        if "}" in i:
            val = i[:leng-1]
        point = list(map(str,val.split(",")))
        result.append(point)
    result.sort(key=lambda x:len(x))
    for i in result:
        for k in i:
            if "{" in k:
                k = k[1:]
            k = int(k)
            if k not in answer:
                answer.append(k)
    return answer
            
    