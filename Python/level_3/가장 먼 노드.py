def solution(n, edge):
    nodes = [[] for _ in range(n + 1)]
    for a, b in edge:
        nodes[a].append(b)
        nodes[b].append(a)
    visit = [0 for _ in range(n + 1)]
    dists = [0 for _ in range(n + 1)]

    que = [1]
    visit[1] = 1

    while que:
        curr = que.pop(0)
        for nn in nodes[curr]:
            if visit[nn]:
                continue
            dists[nn] = dists[curr] + 1
            visit[nn] = 1
            que.append(nn)

    max_edges = max(dists)
    return dists.count(max_edges)

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))