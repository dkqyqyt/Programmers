def solution(n):
    answer = 0
    num = []
    while n != 0:
        num.append(n%3)
        n = n//3
    # print(num)
    three = 1
    for i in range(len(num)-1,-1,-1):
        answer += num[i]*three
        three *= 3

    return answer

n = 45
print(solution(n))