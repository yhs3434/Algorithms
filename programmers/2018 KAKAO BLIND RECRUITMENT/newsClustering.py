# 2018 KAKAO BLIND RECRUITMENT [1차] 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    answer = 0

    orda = ord('a')
    str1 = str1.lower()
    str2 = str2.lower()

    newStr1 = []
    newStr2 = []

    for i in range(len(str1)-1):
        ordCur1 = ord(str1[i]) - orda
        ordCur2 = ord(str1[i+1]) - orda
        if(ordCur1>=0 and ordCur2<26 and ordCur2>=0 and ordCur2<26):
            c1 = str1[i]
            c2 = str1[i+1]
            newStr1.append(c1+c2)
    for i in range(len(str2)-1):
        ordCur1 = ord(str2[i]) - orda
        ordCur2 = ord(str2[i+1]) - orda
        if(ordCur1>=0 and ordCur2<26 and ordCur2>=0 and ordCur2<26):
            c1 = str2[i]
            c2 = str2[i+1]
            newStr2.append(c1+c2)
    newStr1.sort()
    newStr2.sort()
    before = ''
    count = 0
    for i in range(len(newStr1)):
        s = newStr1[i]
        if(before==s):
            count += 1
        else:
            count = 0
        before = s
        newStr1[i] = s + str(count)
    before = ''
    count = 0
    for i in range(len(newStr2)):
        s = newStr2[i]
        if(before==s):
            count += 1
        else:
            count = 0
        before = s
        newStr2[i] = s + str(count)

    a = len(set(newStr1)&set(newStr2))
    b = len(set(newStr1)|set(newStr2))
    j = 0
    if(a==b):
        j = 1
    if(b!=0):
        j = a/b
    answer = int(65536*j)
    return answer

print(solution('aa1+aa2', 'AAAA12'))
print(solution(	"E=M*C^2", "e=m*c^2"))