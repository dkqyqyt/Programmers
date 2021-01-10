def solution(n, results):
    answer = 0
    wins = [set() for _ in range(n + 1)]
    losers = [set() for _ in range(n + 1)]

    for win, lose in results:
        wins[win].add(lose)
        losers[lose].add(win)
    for i in range(1, n + 1):
        for loser in wins[i]:
            losers[loser].update(losers[i])
        for winner in losers[i]:
            wins[winner].update(wins[i])
    for i in range(1, n + 1):
        if len(wins[i]) + len(losers[i]) == n - 1:
            answer += 1
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,results))