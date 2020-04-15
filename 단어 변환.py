from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    word_len = len(begin)
    graph = [[] for _ in range(len(words)+1)]
    for i in range(len(words)):
        same = 0
        for j in range(word_len):
            if begin[j] == words[i][j]:
                same += 1
        if same == word_len-1:
            graph[0].append(i+1)

    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            same = 0
            for k in range(word_len):
                if words[i][k] == words[j][k]:
                    same += 1
            if same == word_len-1:
                print(i,words[i], j,words[j])
                graph[i+1].append(j+1)
    print(graph)
    def bfs(start):
        que = deque()
        visit = [0 for _ in range(len(graph))]
        que.append(start)
        visit[start] = 1
        process = 0
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node != 0 and target == words[node-1]:
                    return process
                for i in range(len(graph[node])):
                    if visit[graph[node][i]]:
                        continue
                    que.append(graph[node][i])
                    visit[graph[node][i]] = 1
            process += 1
        return 0
    answer = bfs(0)
    return answer

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

print(solution(begin, target, words))