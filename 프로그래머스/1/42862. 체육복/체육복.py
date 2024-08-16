def solution(n, lost, reserve):
    # 도난당했지만 여벌 체육복이 있는 학생들을 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
            lost_set.remove(student)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
            lost_set.remove(student)
    
    # 전체 학생 수에서 체육복을 빌리지 못한 학생 수를 뺀 값을 반환
    return n - len(lost_set)
