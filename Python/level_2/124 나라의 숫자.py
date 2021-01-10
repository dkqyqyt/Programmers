def solution(n):
    num = n
    word = ""
    while num > 0:
        if num%3 == 0:
            word = '4'+word
            num = num//3-1
        else:
            word = str(num%3) + word
            num = num//3
    return word

n = 13
print(solution(n))