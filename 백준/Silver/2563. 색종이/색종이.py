paper = [[0] * 100 for _ in range(100)]

# 색종이의 개수 입력
n = int(input())

# 색종이 붙이기
for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):  
        for j in range(y, y + 10):  
            if i < 100 and j < 100:  # 도화지 경계 체크
                paper[i][j] = 1 

black_area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            black_area += 1

print(black_area)
