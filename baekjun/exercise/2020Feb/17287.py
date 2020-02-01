# The Deeper, The Better
# https://www.acmicpc.net/problem/17287
# https://github.com/yhs3434/Algorithms

inp = input()
st = 0

answer = 0
for c in inp:
    if c == '[':
        st += 3
    elif c == '{':
        st += 2
    elif c == '(':
        st += 1
    elif c == ')':
        st -= 1
    elif c == '}':
        st -= 2
    elif c == ']':
        st -= 3
    else:
        if st > answer:
            answer = st
print(answer)