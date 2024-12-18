def solution(s):
    array = list(map(int,s.split()))
    max_val = max(array)
    min_val = min(array)
    return str(min_val) + " " + str(max_val)