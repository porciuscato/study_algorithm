def solution(genres, plays):
    answer = []
    database = {}

    for idx in range(len(genres)):
        genre = genres[idx]
        play = plays[idx]
        if database.get(genre):
            database[genre]['play'] += plays[idx]
            play_list = database[genre]['play_list']
            list_length = len(play_list)
            for check in range(list_length):
                if play > play_list[check][1]:
                    play_list.insert(check, (idx, play))
                    break
            else:
                play_list.append((idx, play))
        else:
            database[genre] = {
                'play': plays[idx],
                'play_list': [(idx, plays[idx])]
                }

    ordered = sorted(database.items(), key=lambda x: x[1]['play'], reverse=True)

    for ele in ordered:
        try:
            for i in range(2):
                answer.append(ele[1]['play_list'][i][0])
        except IndexError:
            pass
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", "electric"], [500, 600, 150, 800, 2500, 4000]))
