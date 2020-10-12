def solution(clothes):
    answer = 1
    data = {}
    for cloth in clothes:
        if cloth[1] in data:
            data[cloth[1]].append(cloth[0])
        else:
            data[cloth[1]] = [cloth[0]]

    for key,value in data.items():
        answer *= len(value)+1

    return answer-1

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
print(solution(clothes))