from math import sqrt
def solution(b, y):
    return [((b+4)/2+sqrt(pow((b+4)/2,2)-4*(b+y)))/2,((b+4)/2-sqrt(pow((b+4)/2,2)-4*(b+y)))/2]

brown = 10
yellow = 2
print(solution(brown,yellow))