N = int(input())
M = int(input())
S = input()

answer = 0

window = 'I'
for i in range(N):
    window += 'IO'

def findPattern(strr):
    l = 0
    r = len(strr) - l
    cnt = 0
    maxNum = 0
    while cnt < len(strr):
        cnt += 1
        lstr = strr[:l + cnt]
        rstr = strr[r - cnt : ]
        # print('lr', lstr, rstr)
        if lstr == rstr:
            maxNum = max(maxNum, cnt)

    return maxNum

def isSame(str1, str2):
    if str1 == str2:
        return True
    return False

i = 0
while i < len(S) - len(window) + 1:
    cur = S[i:i+len(window)]
    if isSame(cur, window):
        answer += 1
        i += 1
    else:
        iplus = findPattern(cur)
        print('cur', cur)
        print('iplus', iplus)
        if iplus == 0 or iplus == len(window):
            i += 1
        else:
            i += (len(window) - iplus)
print(answer)