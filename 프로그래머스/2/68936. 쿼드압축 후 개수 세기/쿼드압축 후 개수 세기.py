def check(arr,y,x,size):
    comp = arr[y][x] 
    for yy in range(y,y+size):
        for xx in range(x,x+size):
            if arr[yy][xx] != comp:
                return False
    return True

def play(arr,size,y,x):
    global cnt_0,cnt_1 
    if check(arr,y,x,size):
        if arr[y][x] == 1:
            cnt_1 += 1
        else:
            cnt_0 += 1
    else:
        ss = size // 2
        play(arr,ss,y,x)
        play(arr,ss,y+ss,x)
        play(arr,ss,y,x+ss)
        play(arr,ss,y+ss,x+ss)
    
    
def solution(arr):
    global cnt_0,cnt_1
    result = []
    cnt_0 = 0
    cnt_1 = 0
    N = len(arr)
    play(arr,N,0,0)
    result.append(cnt_0)
    result.append(cnt_1)
    return result
    
    