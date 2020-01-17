# Ahmed Aly
# https://www.acmicpc.net/problem/10698

n = int(input())
for k in range(1, n+1):
    arr = input().split(' ')
    answer = ''
    if arr[1] == '+':
        if int(arr[0]) + int(arr[2]) == int(arr[4]):
            answer = 'YES'
        else:
            answer = 'NO'
    else:
        if int(arr[0]) - int(arr[2]) == int(arr[4]):
            answer = 'YES'
        else:
            answer = 'NO'
    print('Case',str(k)+':',answer)