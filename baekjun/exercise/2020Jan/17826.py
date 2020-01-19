# 나의 학점은?
# https://www.acmicpc.net/problem/17826
# https://github.com/yhs3434

arr = list(map(int, input().split(' ')))
n = int(input())
arr.sort(reverse=True)
rank = arr.index(n) + 1

if rank <= 5:
    print('A+')
elif rank <=15:
    print('A0')
elif rank <= 30:
    print('B+')
elif rank <= 35:
    print('B0')
elif rank <= 45:
    print('C+')
elif rank <= 48:
    print('C0')
else:
    print('F')