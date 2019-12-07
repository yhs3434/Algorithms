def solution(phone_book):
    answer = True

    book = {}
    for phone in phone_book:
        curPtr = book
        for p in phone:
            if(p not in curPtr):
                curPtr[p] = {'count': 1}
            else:
                curPtr[p]['count'] += 1
            curPtr = curPtr[p]

    for phone in phone_book:
        flag = False
        curPtr = book
        for p in phone:
            if(p in curPtr):
                curPtr = curPtr[p]
            else:
                flag = True
                break
        if(flag==False and curPtr != {'count': 1}):
            answer = False
            break

    return answer

solution(['119', '97674223', '1195524421'])