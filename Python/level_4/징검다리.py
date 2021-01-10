import math


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2

        pre_loc = 0
        min_dist = math.inf
        removed_rocks = 0

        for i in range(len(rocks)):
            dist = rocks[i] - pre_loc
            if dist < mid:
                removed_rocks += 1
            else:
                pre_loc = rocks[i]
                min_dist = min(min_dist, dist)

        if removed_rocks > n:
            right = mid - 1
        else:
            answer = min_dist
            left = mid + 1

    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

print(solution(distance,rocks,n))