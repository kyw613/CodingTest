def solution(players, callings):
    rank = {name:i for i,name in enumerate(players)}
    for c in callings:
        now = rank[c]
        rank[c] -= 1
        rank[players[now-1]] += 1
        players[now],players[now-1] = players[now-1],players[now]
    return players
        
    