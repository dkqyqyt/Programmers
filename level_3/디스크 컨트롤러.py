import heapq
def solution(jobs):
    answer = 0
    que = []
    for job in jobs:
        heapq.heappush(que,job)
    time = 0
    while que:
        temp = []
        while que and que[0][0] <= time:
            temp.append(heapq.heappop(que))
        if not temp:
            start,take = heapq.heappop(que)
            answer += take
            time = start + take
        else:
            temp.sort(key=lambda x:x[1])
            start,take = temp.pop(0)
            answer += time-start+take
            time = time+take
            for job in temp:
                heapq.heappush(que,job)

    return answer//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))