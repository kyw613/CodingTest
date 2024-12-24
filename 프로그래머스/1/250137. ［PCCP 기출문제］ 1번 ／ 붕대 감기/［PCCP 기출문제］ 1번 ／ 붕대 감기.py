def solution(bandage, health, attacks):
    #최대체력은 health 이상 회복 x
    #그러면 attacks 2초부터 시작
    cont = 0 #연속
    idx = 0 # 이게 시간
    init_health = health #초기체력
    
    while attacks:
        time,damage = attacks.pop(0)
        while idx < time:
            idx += 1
            #회복하는거만
            if health + bandage[1] > init_health:
                health = init_health
            else:
                health += bandage[1]
                cont += 1
                if cont == bandage[0]:
                    if health + bandage[2] > init_health:
                        health = init_health
                    else:
                        health += bandage[2]
                        cont = 0
        health -= damage
        cont = 0
        idx += 1
        if health <= 0:
            return -1
    return health
            