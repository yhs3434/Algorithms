# 네 번째 수
# https://www.acmicpc.net/problem/2997
# https://github.com/yhs3434/Algorithms

arr = list(map(int, input().split(' ')))
arr.sort()

if arr[1]-arr[0] == arr[2]-arr[1]:
    print(arr[2]+(arr[1] - arr[0]))
else:
    if arr[1]-arr[0] < arr[2]-arr[1]:
        print(arr[1] + (arr[1]-arr[0]))
    else:
        print(arr[0] + arr[2]-arr[1])