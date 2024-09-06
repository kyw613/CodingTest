def solution(keymap, targets):
    # 각 문자의 최소 키 누름 횟수를 저장할 딕셔너리
    min_press_count = {}
    
    # 각 키에 할당된 문자들을 순회하며 최소 키 누름 횟수 기록
    for i, key in enumerate(keymap):
        for j, char in enumerate(key):
            if char not in min_press_count:
                min_press_count[char] = j + 1  # j + 1이 키 누름 횟수
            else:
                min_press_count[char] = min(min_press_count[char], j + 1)

    # 결과를 담을 리스트
    result = []

    # 각 목표 문자열을 작성하기 위해 필요한 최소 키 누름 횟수 계산
    for target in targets:
        total_presses = 0
        for char in target:
            if char in min_press_count:
                total_presses += min_press_count[char]
            else:
                total_presses = -1
                break
        result.append(total_presses)

    return result
