def solution(phone_book):
    answer = True
    data = {phone_book[0]:0}
    for i in range(1,len(phone_book)):
        # print(data)
        for key in data.keys():
            parse = min(len(key),len(phone_book[i]))
            # print(parse)
            word = phone_book[i][:parse]
            new_key = key[:parse]
            if new_key == word:
                return False
        data[phone_book[i]] = 0

    return answer

phone_book = ['123','12','567','88']

print(solution(phone_book))