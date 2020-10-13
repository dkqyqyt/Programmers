def solution(number, k):
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k == 0:
            answer.append(num)
            continue
        while True:
            if not answer:
                answer.append(num)
                break
            if k == 0:
                answer.append(num)
                break
            if int(answer[-1]) < int(num):
                answer.pop()
                k -= 1
            else:
                answer.append(num)
                break
    if k != 0:
        answer = answer[:-k]

    return ''.join(answer)

number = '1924'
k = 2
print(solution(number,k))