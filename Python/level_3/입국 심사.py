def check_time_people(num, times):
    result = 0
    for time in times:
        result += num // time
    return result


def solution(n, times):
    answer = 0
    left = 0
    right = times[-1] * n + 1

    while left < right:
        mid = (left + right) // 2
        if check_time_people(mid, times) < n:
            left = mid + 1
        else:
            answer = mid
            right = mid
        # print(left, right)
    return answer

n = 6
times = [7,10,15]
print(solution(n,times))