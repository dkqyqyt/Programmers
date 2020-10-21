def solution(numbers):
    answer = 0
    candidates = []
    visit = [0 for _ in range(len(numbers))]
    track(len(numbers), '', visit, candidates, numbers)
    for candidate in candidates:
        if prime_check(int(candidate)):
            answer += 1
    return answer


def prime_check(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def track(max_depth, word, visit, candidates, numbers):
    if word and word not in candidates:
        candidates.append(word)

    if len(word) == max_depth:
        return

    for i in range(len(numbers)):
        if not word and numbers[i] == '0':
            continue
        if visit[i]:
            continue
        visit[i] = 1
        word += numbers[i]
        track(max_depth, word, visit, candidates, numbers)
        word = word[:-1]
        visit[i] = 0

numbers = "17"
print(solution(numbers))