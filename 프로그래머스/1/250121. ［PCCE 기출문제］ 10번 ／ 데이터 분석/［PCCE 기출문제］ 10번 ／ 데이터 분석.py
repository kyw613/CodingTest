def solution(data, ext, val_ext, sort_by):
    result = []
    if ext == "code":
        for i in range(len(data)):
            if data[i][0] < val_ext:
                result.append(data[i])
    elif ext == "date":
        for i in range(len(data)):
            if data[i][1] < val_ext:
                result.append(data[i])
    elif ext == "maximum":
        for i in range(len(data)):
            if data[i][2] < val_ext:
                result.append(data[i])
    elif ext == "remain":
        for i in range(len(data)):
            if data[i][3] < val_ext:
                result.append(data[i])
    if sort_by == "code":
        result.sort(key=lambda x:x[0])
    if sort_by == "date":
        result.sort(key=lambda x:x[1])
    if sort_by == "maximum":
        result.sort(key=lambda x:x[2])
    if sort_by == "remain":
        result.sort(key=lambda x:x[3])
    return result
    