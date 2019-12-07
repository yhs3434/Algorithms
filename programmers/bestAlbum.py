def solution(genres, plays):
    answer = []

    map = {}
    for i in range(len(genres)):
        if (genres[i] in map):
            map[genres[i]]['count'] += plays[i]
            map[genres[i]]['music'].append((i, plays[i]))
        else:
            map[genres[i]] = {'count' : plays[i], 'music': [(i, plays[i])]}
    genreRank = []
    for key in map:
        genreRank.append((key, map[key]['count']))
        map[key]['music'].sort(key=lambda music: music[1], reverse=True)
    genreRank = sorted(genreRank, key=lambda genre: genre[1], reverse=True)

    for genre in genreRank:
        for i in range(2):
            if(len(map[genre[0]]['music'])==1 and i==1):
                break
            answer.append(map[genre[0]]['music'][i][0])

    return answer

solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])