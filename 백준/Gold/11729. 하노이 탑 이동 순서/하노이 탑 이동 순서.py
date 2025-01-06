N = int(input())
#출력은 총 갯수랑 어디서 어디로 움직이는지.. 재귀
#움직임이 비슷하긴 하네 그냥 해야하는게 어떻게든 3번째에 가장 큰것 넣어야하니까..
#1~N을 3에 옮기고싶어.. 그러면 1~N-1을 3이 아닌곳에 다 옮겨야함...
# 끝위치를 어떻게 알지?

def hanoy(n,start,end,help): # 원판 갯수, 시작위치,  끝기둥,보조기둥
    if n == 1:
        print(start,end)
        return
    hanoy(n-1,start,help,end) # n-1개를 보조 기둥에 #3개니까..
    print(start,end)
    hanoy(n-1,help,end,start)
print(2**N-1)
hanoy(N,1,3,2)