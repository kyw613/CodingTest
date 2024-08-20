from collections import deque

def printer_queue(num_cases, cases):
    results = []
    
    for case in cases:
        n, m, priorities = case
        queue = deque([(i, p) for i, p in enumerate(priorities)])
        print_order = 0
        
        while queue:
            current = queue.popleft()
            
            # 현재 문서가 가장 높은 중요도인지 확인
            if any(current[1] < other[1] for other in queue):
                queue.append(current)
            else:
                print_order += 1
                if current[0] == m:
                    results.append(print_order)
                    break
    
    return results

t = int(input())  # 테스트 케이스 수
cases = []

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    cases.append((n, m, priorities))

results = printer_queue(t, cases)
for result in results:
    print(result)
