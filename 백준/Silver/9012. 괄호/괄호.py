N = int(input())

for _ in range(N):
    input_data = input().rstrip()
    count_left = 0
    count_right = 0
    # 처음 시작은 )이 아니어야함
    Val = True # 이것을 사용하여 판단
    Printno = False

    for i in input_data:
        if Val:
            if i ==")":
                Printno = True
                break
        if i =="(":
            count_left += 1
            Val = False
        elif i == ")":
            count_right += 1
            Val = False
        if count_left == count_right:
            Val = True

    if count_left != count_right or Printno == True:
        print("NO")
    else:
        print("YES")
