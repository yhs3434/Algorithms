N = int(input())
arr = list(map(int, input().split(' ')))

M = int(input())
arr2 = list(map(int, input().split(' ')))

answer = []

arr = set(arr)
for elem in arr2:
    if elem in arr:
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a, end=' ')