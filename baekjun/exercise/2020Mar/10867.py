# 중복 빼고 정렬하기
# https://github.com/yhs3434

n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
for a in arr:
    print(a, end=' ')