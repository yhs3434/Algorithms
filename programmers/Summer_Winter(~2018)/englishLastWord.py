# 서머코딩 / 윈터코딩 (~2018) 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]

    befores = []
    cnt = 0
    for word in words:
        if word in befores:
            break
        else:
            if len(befores) != 0:
                if befores[-1][-1] != word[0]:
                    break
                befores.append(word)
            else:
                befores.append(word)
        cnt += 1

    answer[0] = cnt%n + 1
    answer[1] = cnt//n + 1
    if cnt == len(words):
        answer = [0, 0]
    return answer

print(solution(	3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(	5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(	2, ["hello", "one", "even", "never", "now", "world", "draw"]))
