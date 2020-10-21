import heapq


def solution(operations):
    que = []
    for oper in operations:
        action, num = oper.split()
        if action == 'I':
            heapq.heappush(que, int(num))
        else:
            if not que:
                continue
            if num == '1':
                max_num = max(que)
                que.pop(que.index(max_num))
            else:
                heapq.heappop(que)
    if not que:
        return [0, 0]

    return [max(que), min(que)]

operations = ['I 16','D 1']
print(solution(operations))