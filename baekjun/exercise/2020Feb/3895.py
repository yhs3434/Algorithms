# 그리고 하나가 남았다
# https://www.acmicpc.net/problem/3895
# https://github.com/yhs3434/Algorithms

while True:
    n, k, m = map(int, input().split(' '))
    if n==0 and k==0 and m==0:
        break

    arr = [i for i in range(1, n+1)]
    idx = m-1

    while len(arr) > 1:
        del arr[idx]
        idx = (idx + k - 1)%len(arr)
    print(arr[0])