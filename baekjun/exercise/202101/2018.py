n = int(input())

answer = 0
delim = 0
beforeMid = 0
while True:
    delim += 1
    mid = n // delim
    if mid - (delim // 2) < 0:
        break
    l = mid + 1
    r = mid
    flag = False
    val = n
    while val > 0:
        if flag:
            r += 1
            val -= r
            flag = False
        else:
            l -= 1
            val -= l
            flag = True
    if val == 0 and mid != beforeMid:
        answer += 1
    beforeMid = mid

print(answer)