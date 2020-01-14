# 검문
# https://www.acmicpc.net/problem/2981

import sys
rl = sys.stdin.readline

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
nums = []
for xxx in range(n):
    nums.append(int(rl().rstrip()))
nums.sort()
answer = []

if len(nums) == 2:
    val = nums[1] - nums[0]
    for i in range(2, min(nums)+1):
        if val % i == 0:
            answer.append(i)
else:
    newNums = []
    for i in range(1, len(nums)):
        newNums.append(nums[i]- nums[i-1])
    gcdd = getGCD(newNums[0], newNums[1])
    for i in range(2, len(newNums)):
        gcdd = getGCD(gcdd, newNums[i])
    answer.append(gcdd)
    for i in range(2, gcdd//2+1):
        if gcdd%i==0:
            answer.append(i)

answer.sort()
for a in answer:
    print(a, end=' ')