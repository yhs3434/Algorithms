# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True

    st = []
    for p in s:
        if(p=="("):
            st.append(p)
        else:
            if(len(st)==0):
                return False
            else:
                st.pop()
    if(len(st)==0):
        return True
    else:
        return False

