# 가사 검색
#

def solution(words, queries):
    answer = []

    hashes = {}
    hashes2 = {}

    for word in words:
        wordLength = len(word)
        if(wordLength not in hashes):
            hashes[wordLength] = {}
        cur = hashes[wordLength]
        if (wordLength not in hashes2):
            hashes2[wordLength] = {}
        cur2 = hashes2[wordLength]
        for w in word:
            if(w in cur):
                cur[w]['count'] += 1
                cur = cur[w]
            else:
                cur[w] = {'count': 1}
                cur = cur[w]
        for i in range(wordLength):
            i = wordLength - i - 1
            w = word[i]
            if(w in cur2):
                cur2[w]['count'] += 1
                cur2 = cur2[w]
            else:
                cur2[w] = {'count': 1}
                cur2 = cur2[w]


    for query in queries:
        count = [0]
        stack = []
        queryLength = len(query)
        if (query[-1] == '?'):
            if(queryLength in hashes):
                hash = hashes[queryLength]
                stack.append([query, hash, count])
                while stack:
                    curPtr = stack.pop()
                    curQuery = curPtr[0]
                    curHash = curPtr[1]
                    curCount = curPtr[2]
                    if(curQuery==''):
                        curCount[0] += 1
                    else:
                        if(curQuery[0] == '?'):
                            if(curQuery[-1] == '?'):
                                for key in curHash:
                                    if(key!='count'):
                                        curCount[0] += curHash[key]['count']
                            else:
                                for key in curHash:
                                    if(key != 'count'):
                                        stack.append([curQuery[1:], curHash[key], curCount])
                        else:
                            if(curQuery[0] in curHash):
                                stack.append([curQuery[1:], curHash[curQuery[0]], curCount])
        else:
            query = stringReverse(query)
            if (queryLength in hashes2):
                hash = hashes2[queryLength]
                stack.append([query, hash, count])
                while stack:
                    curPtr = stack.pop()
                    curQuery = curPtr[0]
                    curHash = curPtr[1]
                    curCount = curPtr[2]
                    if (curQuery == ''):
                        curCount[0] += 1
                    else:
                        if (curQuery[0] == '?'):
                            if (curQuery[-1] == '?'):
                                for key in curHash:
                                    if (key != 'count'):
                                        curCount[0] += curHash[key]['count']
                            else:
                                for key in curHash:
                                    if (key != 'count'):
                                        stack.append([curQuery[1:], curHash[key], curCount])
                        else:
                            if (curQuery[0] in curHash):
                                stack.append([curQuery[1:], curHash[curQuery[0]], curCount])

        answer.append(count[0])

    return answer

def stringReverse(str):
    newStr = ''
    for s in str:
        newStr = s + newStr
    return newStr

print(solution(['x',"frodo", "front", "frost", "frozen", "frame", "kakao"], ['?', "fro??", "????o", "fr???", "fro???", "pro?", '?????']))