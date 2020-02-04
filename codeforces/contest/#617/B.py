import sys
rl = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = int(rl().rstrip())
    answer = 0
    if s/9 == s//9:
        answer = s + (s//9) - 1
    else:
        answer = s + (s//9)
    print(answer)