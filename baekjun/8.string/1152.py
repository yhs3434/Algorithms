# 단어의 개수
# https://www.acmicpc.net/problem/1152

strr = input().strip()
cnt = 0
flag = False
for c in strr:
    if c == ' ':
        flag = False
    else:
        if flag==False:
            cnt += 1
        flag = True
print(cnt)