# 너의 핸들은
# https://www.acmicpc.net/problem/15819
# https://github.com/yhs3434/Algorithms

n, l = map(int, input().split(' '))
names = []
for _ in range(n):
    names.append(input())
names.sort()
print(names[l-1])