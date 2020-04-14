answer = 0
def track(depth, depth_limit, cur_sum, target):
    global answer
    if depth == depth_limit:
        if cur_sum == target:
            answer += 1
        return

    for i in range(2):
        if i == 0:
            cur_sum += numbers[depth]
            track(depth + 1, depth_limit, cur_sum, target)
            cur_sum -= numbers[depth]
        else:
            cur_sum -= numbers[depth]
            track(depth + 1, depth_limit, cur_sum, target)
            cur_sum += numbers[depth]

def solution(numbers, target):
    track(0, len(numbers), 0, target)


numbers = [1,1,1,1,1]
target = 3
track(0,len(numbers),0,target)

print(answer)