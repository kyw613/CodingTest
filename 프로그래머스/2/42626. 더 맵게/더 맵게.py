import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return result
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + 2 * second
        heapq.heappush(scoville, new_scoville)
        result += 1
    
    if scoville[0] >= K:
        return result
    
    return -1
