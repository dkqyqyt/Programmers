def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = []
    weight_sum = 0
    time = 0
    while len(que) < bridge_length:
        if truck_weights:
            if truck_weights[0] + weight_sum <= weight:
                weight_sum += truck_weights[0]
                que.append(truck_weights.pop(0))
            else:
                que.append(0)
            time += 1
        else:
            que.append(0)

    while que:
        print(que)
        time += 1
        weight_sum -= que.pop(0)
        if truck_weights:
            if truck_weights[0] + weight_sum <= weight:
                weight_sum += truck_weights[0]
                que.append(truck_weights.pop(0))
            else:
                que.append(0)

    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length,weight,truck_weights))