def solution(participant, completion):
    answer = ''
    players = {}
    for p in participant:
        if p in players:
            players[p] += 1
        else:
            players[p] = 1

    for c in completion:
        players[c] -= 1

    for p,count in players.items():
        if count != 0:
            answer = p
    return answer

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']

print(solution(participant,completion))