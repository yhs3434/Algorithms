# 통계학
# https://www.acmicpc.net/problem/2108

import sys
ss = sys.stdin.readline
N = int(ss())
mosts = {}
nums = []
for i in range(N):
    cNum = int(ss())
    nums.append(cNum)
    if cNum not in mosts:
        mosts[cNum] = 1
    else:
        mosts[cNum] += 1
mostCnt = 0
mostNums = []
for key in mosts:
    if mosts[key] > mostCnt:
        mostCnt = mosts[key]
        mostNums = [key]
    elif mosts[key] == mostCnt:
        mostNums.append(key)
mostNums.sort()
nums.sort()

m = round(sum(nums)/N)
print(m)
mid = nums[N//2]
print(mid)
mst = 0
if len(mostNums)>1:
    mst = mostNums[1]
else:
    mst = mostNums[0]
print(mst)

rg = nums[-1] - nums[0]
print(rg)