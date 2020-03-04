# 주사위 게임
# https://github.com/yhs3434

n = int(input())
answer = [100, 100]
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        answer[0] -= b
    elif a > b:
        answer[1] -= a

for a in answer:
    print(a)