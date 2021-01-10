def solution(answers):
    rules = [
        0,
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    repeat = [0,5,8,10]
    correct = [0,0,0,0]
    for i,answer in enumerate(answers):
        for j in range(1,4):
            if answer == rules[j][i%repeat[j]]:
                correct[j] += 1
    max_correct = correct[1]
    result = [1]
    for i in range(2,4):
        if correct[i] > max_correct:
            max_correct = correct[i]
            result = [i]
        elif correct[i] == max_correct:
            result.append(i)
    return result

answers = [1,2,3,4,5]
print(solution(answers))