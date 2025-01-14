def solution(dirs):
    # 처음걸어본 길의 길이 만약 나가는 경우에는 그냥 명령 무시한다.
    pos_dict = {"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    #L,R,U,D별로 넣는거야 그래서 만약에 있으면 이동은 하지만 total은 안오르는걸로
    total = 0
    U = {}
    D = {}
    R = {}
    L = {}
    now_y,now_x = 0,0
    for i in dirs:
        dy,dx = pos_dict[i]
        if i == "U":
            ny = now_y + dy
            nx = now_x + dx
            if -5 <= ny <=5 and -5 <= nx <= 5:
                if (now_y,now_x) not in U and (now_y+1,now_x) not in D:
                    U[(now_y,now_x)] = 1
                    D[(now_y+1,now_x)] = 1
                    total += 1
                now_y, now_x = ny,nx
        if i == "D":
            ny = now_y + dy
            nx = now_x + dx
            if -5 <= ny <=5 and -5 <= nx <= 5:
                if (now_y,now_x) not in D and (now_y-1,now_x) not in U:
                    D[(now_y,now_x)] = 1
                    U[(now_y-1,now_x)] = 1
                    total += 1
                now_y, now_x = ny,nx
        if i == "R":
            ny = now_y + dy
            nx = now_x + dx
            if -5 <= ny <=5 and -5 <= nx <= 5:
                if (now_y,now_x) not in R and (now_y,now_x+1) not in L:
                    R[(now_y,now_x)] = 1
                    L[(now_y,now_x+1)] = 1
                    total += 1
                now_y, now_x = ny,nx
        if i == "L":
            ny = now_y + dy
            nx = now_x + dx
            if -5 <= ny <=5 and -5 <= nx <= 5:
                if (now_y,now_x) not in L and (now_y,now_x-1) not in R:
                    L[(now_y,now_x)] = 1
                    R[(now_y,now_x-1)] = 1
                    total += 1
                now_y, now_x = ny,nx
    return total