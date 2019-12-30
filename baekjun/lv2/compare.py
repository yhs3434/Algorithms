# 두 수 비교하기
# https://www.acmicpc.net/problem/1330

nums = list(map(int, input().split(' ')))
n1 = nums[0]
n2 = nums[1]

if n1 < n2:
    print('<')
elif n1 > n2:
    print('>')
else:
    print('==')