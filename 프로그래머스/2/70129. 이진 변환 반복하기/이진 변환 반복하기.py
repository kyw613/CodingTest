def solution(s):
    cnt = 0  # 변환 횟수
    cnt_0 = 0  # 제거된 0의 개수

    while s != "1":
        cnt += 1
        cnt_0 += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]

    return [cnt, cnt_0]