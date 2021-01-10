def solution(n, lost, reserve):
    answer = 0
    s = [1 for _ in range(n + 1)]
    for i in lost:
        s[i] -= 1
    for i in reserve:
        s[i] += 1

    for i in range(1, len(s)):
        if s[i] > 0:
            answer += 1
            continue
        if s[i] == 0:
            if i - 1 != 0 and s[i - 1] == 2:
                s[i - 1] -= 1
                s[i] += 1
                answer += 1
                continue
            if i + 1 < len(s) and s[i + 1] == 2:
                s[i + 1] -= 1
                s[i] += 1
                answer += 1
                continue

    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n,lost,reserve))