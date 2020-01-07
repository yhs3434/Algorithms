# 찾아라 프로그래밍 마에스터 - 사칙연산
# https://programmers.co.kr/learn/courses/30/lessons/1843

def solution(arr):
    dpmax = [[0 for j in range(len(arr))] for i in range(len(arr))]
    dpmin = [[0 for j in range(len(arr))] for i in range(len(arr))]
    nums = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] == '+':
            nums[i] = 2000
        elif arr[i] == '-':
            nums[i] = 3000
        else:
            nums[i] = int(arr[i])
            dpmax[i][i] = int(arr[i])
            dpmin[i][i] = int(arr[i])

    for i in range(2, len(arr), 2):
        for j in range(0, len(arr)-i, 2):
            maxVal = -float('inf')
            minVal = float('inf')
            maxTemp = 0
            minTemp = 0
            for k in range(j, j+i):
                if k%2==0:
                    continue
                if nums[k] == 2000:
                    maxTemp = dpmax[j][k-1] + dpmax[k+1][i+j]
                    minTemp = dpmin[j][k-1] + dpmin[k+1][i+j]
                elif nums[k] == 3000:
                    maxTemp = dpmax[j][k-1] - dpmin[k+1][i+j]
                    minTemp = dpmin[j][k-1] - dpmax[k+1][i+j]
                if maxTemp > maxVal:
                    maxVal = maxTemp
                if minTemp < minVal:
                    minVal = minTemp
            dpmax[j][i+j] = maxVal
            dpmin[j][i+j] = minVal
    answer = dpmax[0][-1]

    return answer


print(solution(['1', '-', '3', '+', '5', '-', '8']))