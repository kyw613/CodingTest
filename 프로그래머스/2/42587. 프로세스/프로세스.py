def solution(priorities, location):
    # 우선순위와 위치를 함께 리스트에 넣음
    pri = [(i, priority) for i, priority in enumerate(priorities)]
    cnt = 0

    while pri:
        # 현재 프로세스의 우선순위가 가장 높은지 확인
        if pri[0][1] == max(pri, key=lambda x: x[1])[1]:
            cnt += 1
            # 현재 프로세스를 실행해야 하는 경우
            if pri[0][0] == location:
                return cnt
            else:
                pri.pop(0)  # 프로세스를 큐에서 제거
        else:
            pri.append(pri.pop(0))  # 프로세스를 큐의 맨 뒤로 이동

