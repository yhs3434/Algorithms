# K번째 수
# https://www.acmicpc.net/problem/11004
# https://github.com/yhs3434/Algorithms

n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()
print(arr[k-1])