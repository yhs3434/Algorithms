# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    answer = 0
    length = len(words)
    wordLength = len(words[0])
    counts = []

    if (target not in words):
        return 0

    setWords = []
    for i in range(length):
        word = words[i]
        setWords.append(set(list(word)))

    stack = [[begin, 0, []]]
    while stack:
        curPtr = stack.pop()
        curWord = curPtr[0]
        if(curWord == target):
            counts.append(curPtr[1])
            continue
        for i in range(length):
            if(i not in curPtr[2]):
                tempCount = 0
                for j in range(wordLength):
                    if(curWord[j]==words[i][j]):
                        tempCount += 1
                if(tempCount == (wordLength-1)):
                    stack.append([words[i], curPtr[1]+1, curPtr[2]+[i]])
    if(len(counts)==0):
        return 0
    answer = min(counts)
    return answer

print(solution('hit', 'cog', ['hot', 'dto', 'odg', 'lot', 'lgo', 'cog']))
print(solution('hit', 'hhh', ['hhh','hht']))