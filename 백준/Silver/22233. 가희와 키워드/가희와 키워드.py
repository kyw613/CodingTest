N, M = map(int, input().split())

# 키워드를 set으로 저장
save = set(input() for _ in range(N))
count = N  # 남은 키워드 수

# M번의 삭제 요청 처리
for _ in range(M):
    a = input().split(",")
    for t in a:
        if t in save:  # 키워드가 남아있을 경우
            save.remove(t)  # 사용된 키워드 제거
            count -= 1  # 남은 키워드 수 감소
    print(count)  # 각 입력 후 남은 키워드 수 출력
