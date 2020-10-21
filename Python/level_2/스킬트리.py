def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        if skill_check(skill,skill_tree):
            answer += 1
    return answer

def skill_check(skill,skill_tree):
    learn = [0 for _ in range(len(skill))]
    for char in skill_tree:
        if char not in skill:
            continue
        for i in range(len(learn)):
            if skill[i] == char:
                learn[i] = 1
                break
            if not learn[i]:
                return False
    return True

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill,skill_trees))