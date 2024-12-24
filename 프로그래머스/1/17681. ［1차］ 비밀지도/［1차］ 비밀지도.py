def solution(n, arr1, arr2):
    save = []
    answer = []
    #1. arr1,arr2를 각각 2진수로 치환.
    #이중 가장 긴값을 n으로 둔다.
    #두개를 and 연산한후 1을 #으로 0을 공백으로 바꾸어 리턴하기
    n = 0
    for a1,a2 in zip(arr1,arr2):
        result = bin(a1 | a2)[2:]
        save.append(result)
        n = max(n,len(result))
    for s in save:
        if len(s) != n:
            s = str((n-len(s)) * "0" + s)    
        s=s.replace("1","#").replace("0"," ")
        answer.append(s)
        
    return answer
    
