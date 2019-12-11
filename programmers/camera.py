# 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

from heapq import heappush, heappop

def solution(routes):
    answer = 0

    routesLeft = sorted(routes, key=lambda route:route[0])
    routesRight = sorted(routes, key=lambda route:route[1])

    turn = 'l'
    while(routesLeft):
        answer += 1
        if(turn == 'l'):
            cameraPoint = routesLeft[-1][0]
            length = len(routesLeft)
            for i in range(length):
                j = length-i-1
                if(isGap(cameraPoint, routesLeft[j])):
                    del routesLeft[j]
                if(isGap(cameraPoint, routesRight[j])):
                    del routesRight[j]
            turn = 'r'
        else:
            cameraPoint = routesRight[0][1]
            length = len(routesLeft)
            for i in range(length):
                j = length - i - 1
                if (isGap(cameraPoint, routesLeft[j])):
                    del routesLeft[j]
                if (isGap(cameraPoint, routesRight[j])):
                    del routesRight[j]
            turn = 'l'

    return answer

def isGap(val,route):
    if(route[0]<=val and val<=route[1]):
        return True
    else:
        return False

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3], [3, 10], [2, 20]]))