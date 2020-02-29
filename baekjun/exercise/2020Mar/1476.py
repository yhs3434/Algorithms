# 날짜 계산
# https://www.acmicpc.net/problem/1476
# https://github.com/yhs3434/Algorithms

E, S, M = map(int, input().split(' '))
RANGE = 15*28*19
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0

arr1 = []
n = E
while n <= RANGE:
    arr1.append(n)
    n += 15
arr2 = []
for a in arr1:
    if a%28==S:
        arr2.append(a)
arr3 = []
for a in arr2:
    if a%19 == M:
        arr3.append(a)
if len(arr3)>=2 and arr3[0] == 0:
    arr3[0] = arr3[1]
print(arr3[0])