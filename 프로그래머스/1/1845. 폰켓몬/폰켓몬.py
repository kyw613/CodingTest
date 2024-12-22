def solution(nums):
    #중복
    #N//2와 중복제거해서 한것중 작은거 선택
    pocketmon = set(nums)
    result = min(len(pocketmon),len(nums)//2)
    return result