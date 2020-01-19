# 고려대학교에는 공식 와인이 있다
# https://www.acmicpc.net/problem/16673
# https://github.com/yhs3434

c, k, p = map(int, input().split(' '))
sumVal = 0

for i in range(1, c+1):
    sumVal += (k*i + p*i*i)
print(sumVal)