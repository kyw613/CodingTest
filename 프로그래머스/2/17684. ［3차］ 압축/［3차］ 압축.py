def solution(msg):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_dict = {}
    for i in range(len(alpha)):
        alpha_dict[alpha[i]] = i + 1
    num_idx = 26
    result = []
    
    while msg:
        idx = 0
        i = 1
        while True:
            if idx + i > len(msg) or msg[idx:idx + i] not in alpha_dict:
                break
            i += 1
        
        to_idx = alpha_dict[msg[idx:idx + i - 1]]
        result.append(to_idx)
        
        if idx + i <= len(msg):
            alpha_dict[msg[idx:idx + i]] = num_idx + 1
            num_idx += 1
        
        msg = msg[idx + i - 1:]
    
    return result
