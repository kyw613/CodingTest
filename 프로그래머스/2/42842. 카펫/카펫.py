def solution(brown, yellow):
    #노란색의 약수를 찾으면 크기를 알수있는데 
    for i in range(1,int(yellow**0.5) + 1):
        if yellow % i == 0:
            if brown == (i + yellow // i) *2 + 4:
                return [yellow//i+2,i+2]
                