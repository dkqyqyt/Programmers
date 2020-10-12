import math
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    print(days)
    count = 0
    index = 0
    now = 0
    while now < len(days) and index < len(days):
        # print(now,index)
        if days[index] <= days[now]:
            count += 1
            index += 1
        else:
            now = index
            answer.append(count)
            count = 0
    if count != 0:
        answer.append(count)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses,speeds))