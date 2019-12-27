# 2017 팁스타운 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 0

    st = []
    for c in s:
        if not st:
            st.append(c)
        else:
            if st[-1] == c:
                st.append(c)
                stUpdate(st, len(st))
            else:
                st.append(c)
    if st:
        return 0
    else:
        return 1

    return answer

def stUpdate(st, size):
    if size<2:
        return
    if st[-1] == st[-2]:
        st.pop()
        st.pop()
        stUpdate(st, size-2)

print(solution("baabaa"))
print(solution("cdcd"))