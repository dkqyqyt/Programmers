def solution(priorities, location):
    answer = 0
    my_priorities = []
    for i,priority in enumerate(priorities):
        my_priorities.append((priority,i))

    count = 1
    for i in range(len(my_priorities)):
        print(my_priorities)
        importance = my_priorities[0][0]
        index = 0
        for j in range(1,len(my_priorities)):
            if my_priorities[j][0] > importance:
                importance = my_priorities[j][0]
                index = j
        if my_priorities[index][1] == location:
            return count
        count += 1
        my_priorities = my_priorities[index+1:] + my_priorities[:index]
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities,location))