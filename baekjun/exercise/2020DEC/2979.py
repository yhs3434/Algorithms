A, B, C = map(int, input().split())
d = [0] * (101)
for i in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        d[i] += 1

answer = 0
for i in range(101):
    if d[i] == 1:
        answer += A
    elif d[i] == 2:
        answer += 2*B
    elif d[i] == 3:
        answer += 3*C
print(answer)