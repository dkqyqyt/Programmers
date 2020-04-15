def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]

    def dfs(start):
        stack = []
        stack.append(start)
        visit[start] = 1

        while stack:
            start = stack.pop()
            for i in range(len(computers[start])):
                if start == i or not computers[start][i]:
                    continue
                if visit[i]:
                    continue
                visit[i] = 1
                stack.append(i)

    for i in range(n):
        if visit[i]:
            continue
        dfs(i)
        answer += 1
    return answer

n = 3
computers = [[1,1,0],[1,1,0],[0,0,1]]

print(solution(n,computers))