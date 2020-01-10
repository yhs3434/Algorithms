# 블랙잭
# https://www.acmicpc.net/problem/2798

import queue

def solution(n, m, cards):
    answer = 0

    #q = queue.Queue()
    #q.put((0, 0, []))
    st = []
    st.append((0, 0, []))
    while st:
        cur = st.pop()
        cN = cur[0]
        cCnt = cur[1]
        cCards = cur[2]

        if cCnt == 3:
            if cN <= m:
                if cN > answer:
                    answer = cN
                    if answer == m:
                        return answer

        if cCnt < 3 and cN < m:
            for card in cards:
                if card not in cCards:
                    if cN+card <= m:
                        st.append((cN+card, cCnt+1, cCards+[card]))

    return answer

n, m = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))
print(solution(n, m, cards))