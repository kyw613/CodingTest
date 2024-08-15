def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m=len(a[0])
    result = [ [0]* n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length * 2):
        for j in range(lock_length,lock_length * 2):
            if new_lock[i][j] !=1:
                return False
    return True


def solution(key, lock):
    answer = True
    #0은 홈부분 1은 돌기부분
    #key를 돌리고 움직이는게 필요 
    #열쇠 돌기가 키의 홈과 맞아아한다
    n = len(lock)
    m = len(key)
    new_lock =  [ [0]* (n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                    
    return False