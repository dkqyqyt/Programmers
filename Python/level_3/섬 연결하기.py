def find(node, parents):
    if parents[node] < 0:
        return node
    parents[node] = find(parents[node], parents)
    return parents[node]


def union(x, y, parents):
    x = find(x, parents)
    y = find(y, parents)

    if x == y:
        return True
    else:
        if x > y:
            parents[y] = x
        else:
            parents[x] = y
    return False


def solution(n, costs):
    answer = 0
    edges = 0
    costs.sort(key=lambda x: x[2])
    parents = [-1 for _ in range(n)]
    for a, b, dist in costs:
        if not union(a, b, parents):
            edges += 1
            answer += dist

        if edges == n - 1:
            break
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))