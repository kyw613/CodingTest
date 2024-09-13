def solution(routes):
    # 차량 경로를 진출 지점을 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    cnt = 0  # 카메라 설치 횟수
    camera = -30001  # 초기 카메라 위치를 경로의 범위 밖으로 설정

    # 각 차량의 경로를 확인
    for route in routes:
        # 현재 카메라가 해당 차량의 경로에 포함되지 않는 경우
        if camera < route[0]:
            cnt += 1  # 새로운 카메라 설치
            camera = route[1]  # 카메라를 현재 차량의 진출 지점에 설치

    return cnt