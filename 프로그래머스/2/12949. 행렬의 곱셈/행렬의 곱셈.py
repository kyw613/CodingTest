def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)): # 1-행
        save = []
        for t in range(len(arr2[0])):
            total = 0
            for k in range(len(arr1[0])): # 1-열 = 2-행
                total += arr1[i][k] * arr2[k][t]
            save.append(total)
        result.append(save)
    return result