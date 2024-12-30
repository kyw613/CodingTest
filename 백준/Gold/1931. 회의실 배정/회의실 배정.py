# 회의의 개수 N 입력
N = int(input())

meetings = []

for _ in range(N):
    s, f = map(int, input().split())
    meetings.append((s, f))
#정렬
meetings.sort(key=lambda x: (x[1], x[0]))

result = 0
end_time = 0

for s, f in meetings:
    if s >= end_time:
        end_time = f
        result += 1

print(result)
