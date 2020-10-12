def solution(genres, plays):
    answer = []
    data = {}
    playtime = {}
    for i,genre_play in enumerate(zip(genres,plays)):
        if genre_play[0] in data:
            data[genre_play[0]].append((genre_play[1],i))
            playtime[genre_play[0]] += genre_play[1]
        else:
            data[genre_play[0]] = [(genre_play[1],i)]
            playtime[genre_play[0]] = genre_play[1]
    for key,val in data.items():
        data[key] = sorted(val, key=lambda x:-x[0])
    # print(data)
    playtime = sorted(list(playtime.items()), key=lambda x:-x[1])
    # print(playtime)
    for a in playtime:
        for i,index in enumerate(data[a[0]]):
            if i == 2:
                break
            answer.append(index[1])
    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))