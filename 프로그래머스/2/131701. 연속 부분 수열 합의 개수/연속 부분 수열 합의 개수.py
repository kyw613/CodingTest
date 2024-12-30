def solution(elements):
    # 길게 추가해주면 되나? 
    elements += elements
    print(elements)
    result = []
    for k in range(len(elements) // 2):
        # k+1은 사이즈 길이
        total = 0
        for i in range(0,len(elements) - (k+1)):
            total = sum(elements[i:i+k+1])
            result.append(total)
    return len(set(result))
        
        