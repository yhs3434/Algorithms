def solution(words, queries):
    newQueries = []
    answer = []

    newWords_h = [[[] for i in range(10000)] for i in range(26)]
    # 접두
    newWords_t = [[[] for i in range(10000)] for i in range(26)]
    # 접미

    for word in words:
        w_h = word[0]
        w_t = word[-1]
        newWords_h[ord(w_h)-ord('a')][len(word)-1].append(word)
        newWords_t[ord(w_t)-ord('a')][len(word)-1].append(word)

    for query in queries:
        value = query.replace('?', '')
        if(query[0]==query[len(query)-1]):
            newQuery = {'value':value, 'head':2, 'length':len(query), 'vLength':len(value)}
            answer.append(howMany(words, newQuery))
        elif(query[0]=='?'):
            newQuery = {'value':value, 'head':1, 'length':len(query), 'vLength':len(value)}
            answer.append(howMany(newWords_t[ord(value[-1])-ord('a')][len(query)-1], newQuery))
        else:
            newQuery = {'value':value, 'head':0, 'length':len(query), 'vLength':len(value)}
            answer.append(howMany(newWords_h[ord(value[0])-ord('a')][len(query)-1], newQuery))
        # 0: 접두
        # 1: 접미
        # 2: 전체가 ?

    return answer

def howMany(words, query):
    query_length = query['length']
    query_value = query['value']
    query_head = query['head']
    headLength = query['vLength']
    count = 0
    for word in words:
        if(len(word)!=query_length):
            continue
        else:
            if(query_head==0):
                if(word[:headLength]==query_value):
                    count+=1
            elif(query_head==1):
                if(word[-headLength:]==query_value):
                    count+=1
            else:
                if(word==query_value):
                    count+=1
    return count



print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))