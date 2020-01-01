# 2019 KAKAO BLIND RECRUITMENT 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    dic = {}
    answer = []
    for text in record:
        textArr = text.split(' ')
        if(textArr[0] == 'Enter'):
            dic[textArr[1]] = textArr[2]
        elif(textArr[0] == 'Change'):
            dic[textArr[1]] = textArr[2]

    for text in record:
        textArr = text.split(' ')
        if (textArr[0] == 'Enter'):
            answer.append('%s님이 들어왔습니다.' % dic[textArr[1]])
        elif (textArr[0] == 'Leave'):
            answer.append('%s님이 나갔습니다.' % dic[textArr[1]])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))