# 짝수를 찾아라
# https://www.acmicpc.net/problem/3058
# https://github.com/yhs3434/Algorithms

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split(' ')))
    newArr = []
    for a in arr:
        if a % 2 == 0:
            newArr.append(a)
    newArr.sort()
    print(sum(newArr), newArr[0])