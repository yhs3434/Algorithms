from collections import deque

def solution(user_id, banned_id):
    answer = 0
    arr = []
    for id in banned_id:
        lenn = len(id)
        avail = {}
        cur = avail
        for c in id:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        temp = []
        for id in user_id:
            if len(id) != lenn:
                continue
            flag = True
            cur = avail
            for c in id:
                if '*' in cur:
                    cur = cur['*']
                else:
                    if c in cur:
                        cur = cur[c]
                    else:
                        flag = False
            if flag:
                temp.append(id)
        arr.append(temp)

    q = deque()
    q.append((set([]), 0))   # (ids, cnt)
    arr2 = []
    while q:
        cur = q.popleft()
        ids = cur[0]
        cnt = cur[1]

        if cnt < len(arr):
            for i in range(len(arr[cnt])):
                idd = arr[cnt][i]
                if idd not in ids:
                    q.append((ids|{idd}, cnt+1))
        else:
            arr2.append(ids)
    answerId = []
    while arr2:
        curId = arr2.pop()
        answerId.append(curId)
        temp = []
        while arr2:
            iddd = arr2.pop()
            if len(iddd)==len(curId) and len(iddd & curId)==len(iddd):
                continue
            else:
                temp.append(iddd)
        arr2 = temp
    answer = len(answerId)

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))