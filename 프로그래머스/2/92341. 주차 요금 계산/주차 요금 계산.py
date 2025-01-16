import math
def solution(fees, records):
    in_dict = {}
    result_dict = {}
    result = []
    for record in records:
        time,car,ty = record.split()
        if ty == "IN":
            in_dict[car] = time
            if car not in result_dict:
                result_dict[car] = 0
        else:
            h,m = time.split(":")
            prev_h,prev_m = in_dict[car].split(":")
            result_dict[car] += (int(h)-int(prev_h)) * 60 + int(m)-int(prev_m)
            del(in_dict[car])
    for car,time in in_dict.items():
        prev_h,prev_m = time.split(":")
        result_dict[car] += (int(23)-int(prev_h)) * 60 + int(59)-int(prev_m)
    for c,t in sorted(result_dict.items(),key=lambda x:x[0]):
        a=(fees[1] + math.ceil((int(t)-fees[0])/ fees[2]) *fees[3] )
        if a <= fees[1]:
            result.append(fees[1])
        else:
            result.append(a)
    return result
        
        