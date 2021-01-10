def solution(n, edge):
    graph = [[] for _ in range(n+1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    dist = [-1 for _ in range(n+1)]
    dist[1] = 0
    que = [1]

    while que:
        cur = que.pop(0)
        for n in graph[cur]:
            if dist[n] != -1:
                continue
            dist[n] = dist[cur] + 1
            que.append(n)

    max_dist = max(dist)
    count = 0
    for i in range(len(dist)):
        if dist[i] == max_dist:
            count += 1
    return count

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))