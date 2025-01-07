def solution(cacheSize, cities):
    cache = []
    total = 0
    for i in cities:
        i = i.lower()
        if i in cache:
            total += 1
            cache.remove(i)
            cache.append(i)
        else:
            cache.append(i)
            total += 5
            if len(cache) > cacheSize:
                cache.pop(0)
    return total
                
        