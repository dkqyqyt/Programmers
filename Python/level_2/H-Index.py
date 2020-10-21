def solution(citations):
    answer = 0
    citations.sort()
    for h in range(10000,-1,-1):
        index = 0
        while index < len(citations) and citations[index] < h:
            index += 1
        up = len(citations)-index
        if up >= h:
            return h

citations = [3, 0, 6, 1, 5]
print(solution(citations))