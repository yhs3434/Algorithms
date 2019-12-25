# 2018 KAKAO BLIND RECRUITMENT [3차] 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    answer = [' ' for i in range(len(files))]

    newFiles = []
    fileIdx = -1
    for file in files:
        fileIdx += 1
        flag = False
        flag2 = False
        i = 0
        j = 0
        for f in file:
            if ord(f)>=ord('0') and ord(f)<=ord('9'):
                if(flag == False):
                    flag = True
            else:
                if(flag==True and flag2 == False):
                    flag2 = True
            if(flag==True):
                if(flag2!=True):
                    j += 1
            else:
                i += 1
                j += 1
        newFiles.append([file[:i].lower(), int(file[i:j]), file[j:], fileIdx])
    newFiles.sort(key=lambda key:key[1])
    newFiles.sort(key=lambda key:key[0])
    i = -1
    for file in newFiles:
        i += 1
        answer[i] = files[file[3]]
    return answer

print(solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(	["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))