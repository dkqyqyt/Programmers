def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(reverse=True, key=lambda x:x*3)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)

numbers = [6, 10, 2]
print(solution(numbers))