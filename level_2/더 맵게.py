import heapq

def solution(scoville, K):
    answer = 0
    prior_que = []
    for scov in scoville:
        heapq.heappush(prior_que,scov)

    while True:
        if check(prior_que,K):
            break
        answer += 1
        low_scov = heapq.heappop(prior_que)
        low_scov_1 = heapq.heappop(prior_que)
        new_scov = low_scov + low_scov_1*2
        if not prior_que:
            if new_scov < K:
                return -1
        heapq.heappush(prior_que,new_scov)
    return answer

def check(que,k):
    for scov in que:
        if scov < k:
            return False
    return True
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))

