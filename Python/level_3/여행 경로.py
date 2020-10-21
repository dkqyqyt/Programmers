def track(depth, tickets, visit, path, paths):
    # print(path,depth)
    if depth == len(tickets):
        # print(path)
        tmp = []
        for a in path:
            tmp.append(a)
        paths.append(tmp)
        return

    for i in range(len(tickets)):
        if visit[i]:
            continue
        if tickets[i][0] == path[-1]:
            visit[i] = 1
            path.append(tickets[i][1])
            track(depth+1, tickets, visit, path,paths)
            path.pop()
            visit[i] = 0

# check = []
def solution(tickets):
    answer = []
    tickets.sort()
    paths = []
    visit = [0 for _ in range(len(tickets))]
    track(0,tickets,visit,['ICN'],paths)
    # print(paths)
    answer = paths[0]
    return answer

# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))