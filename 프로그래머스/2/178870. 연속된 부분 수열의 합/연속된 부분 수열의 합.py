def solution(sequence, k):
    # 투포인터
    left_idx = 0
    right_idx = 0
    total = 0
    min_val = float('inf')
    x, y = 0, 0
    
    while left_idx < len(sequence):
        while right_idx < len(sequence) and total < k:
            total += sequence[right_idx]
            right_idx += 1
        
        # total  k 비교
        if total == k:
            le = right_idx - left_idx
            if le < min_val:
                min_val = le
                x, y = left_idx, right_idx - 1
        total -= sequence[left_idx]
        left_idx += 1
    
    return x, y
