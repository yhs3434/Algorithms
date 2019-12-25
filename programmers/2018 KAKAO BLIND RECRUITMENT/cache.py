# 2018 KAKAO BLIND RECRUITMENT [1차] 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    if(cacheSize == 0):
        return len(cities) * 5

    cache = {}
    idx = -1
    for city in cities:
        city = city.lower()
        idx += 1
        if (city not in cache):
            if (len(cache) == cacheSize):
                minKey = ''
                minIdx = float('inf')
                for key in cache:
                    if (cache[key] < minIdx):
                        minIdx = cache[key]
                        minKey = key
                del cache[minKey]
            cache[city] = idx
            answer += 5

        else:
            cache[city] = idx
            answer += 1

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(	3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))