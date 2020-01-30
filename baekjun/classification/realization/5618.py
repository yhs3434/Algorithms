# 공약수
# https://www.acmicpc.net/problem/5618
# https://github.com/yhs3434/Algorithms

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
arr = list(map(int, input().split(' ')))
gcdd = arr[0]
for i in range(1, n):
    gcdd = getGCD(gcdd, arr[i])

answer = set()
for i in range(1, int(gcdd**0.5)+1):
    if gcdd%i == 0:
        answer.add(i)
        answer.add(gcdd//i)
answer = sorted(list(answer))
for a in answer:
    print(a)