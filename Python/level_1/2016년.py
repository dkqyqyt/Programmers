def solution(a, b):
    answer = ''
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    date = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    total_days = 0
    month = 1
    while month < a:
        total_days += days[month]
        month += 1
    # print(total_days)
    total_days += b
    # print(total_days)
    answer = date[total_days%7]
    return answer

a = 5
b = 24
print(solution(a,b))