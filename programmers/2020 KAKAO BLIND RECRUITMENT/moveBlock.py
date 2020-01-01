# 2020 KAKAO BLIND RECRUITMENT 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063

# (r, c, 0) : 가로 , (r, c, 1) : 세로

import queue
import numpy as np

def solution(board):
    answer = 0

    robot = (0, 1, 0)
    dpBoard = [[[float('inf'), float('inf')] for j in range(len(board))] for i in range(len(board))]
    answer = goMove(robot, board, dpBoard)

    return answer

def goMove(robot, board, dpBoard):
    bLen = len(board)

    q = queue.Queue()
    minCnt = float('inf')

    q.put((robot, 'up', 0, [robot]))
    q.put((robot, 'right', 0, [robot]))
    q.put((robot, 'down', 0, [robot]))
    q.put((robot, 'left', 0, [robot]))

    while not q.empty():
        cur = q.get()
        cRobot = cur[0]
        cDirection = cur[1]
        cCnt = cur[2]
        cMoved = cur[3]
        r = cRobot[0]
        c = cRobot[1]
        hv = cRobot[2]

        if r == bLen - 1 and c == bLen - 1:
            if cCnt < minCnt:
                minCnt = cCnt
        if cCnt >= minCnt:
            continue
        newRobots = []
        newRobots.extend(moveDirection(cRobot, cDirection, board))
        for newRobot in newRobots:
            nr = newRobot[0]
            nc = newRobot[1]
            nhv = newRobot[2]
            if cCnt + 1 < dpBoard[nr][nc][nhv]:
                dpBoard[nr][nc][nhv] = cCnt + 1
                q.put((newRobot, 'down', cCnt + 1, cMoved + [newRobot]))
                q.put((newRobot, 'left', cCnt + 1, cMoved + [newRobot]))
                q.put((newRobot, 'up', cCnt + 1, cMoved+[newRobot]))
                q.put((newRobot, 'right', cCnt + 1, cMoved + [newRobot]))
    return minCnt

def moveDirection(robot, direction, board):
    r = robot[0]
    c = robot[1]
    hv = robot[2]

    newRobots = []

    if direction == 'up':
        if isAvail(robot, direction, board):
            if hv == 0:
                newRobots = [(r-1, c, 0), (r, c, 1), (r, c-1, 1)]
                #for newRobot in newRobots:
                #    if newRobot not in moved:
                #        moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
            elif hv == 1:
                newRobots = [(r-1, c, 1)]
                #if newRobot not in moved:
                #    moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
    elif direction == 'right':
        if isAvail(robot, direction, board):
            if hv == 0:
                newRobots = [(r, c+1, 0)]
                #if newRobot not in moved:
                #    moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
            elif hv == 1:
                newRobots = [(r, c+1, 1), (r-1, c+1, 0), (r, c+1, 0)]
                #for newRobot in newRobots:
                #   if newRobot not in moved:
                #        moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
    elif direction == 'down':
        if isAvail(robot, direction, board):
            if hv == 0:
                newRobots = [(r+1, c, 0), (r+1, c, 1), (r+1, c-1, 1)]
                #for newRobot in newRobots:
                #    if newRobot not in moved:
                #        moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
            elif hv == 1:
                newRobots = [(r+1, c, 1)]
                #if newRobot not in moved:
                #    moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
    elif direction == 'left':
        if isAvail(robot, direction, board):
            if hv == 0:
                newRobots = [(r, c-1, 0)]
                #if newRobot not in moved:
                #    moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #    moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
            elif hv == 1:
                newRobots = [(r, c-1, 1), (r-1, c, 0), (r, c, 0)]
                #for newRobot in newRobots:
                #    if newRobot not in moved:
                #        moveDirection(newRobot, 'up', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'right', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'down', board, cnt + 1, moved+[newRobot], minCnt)
                #        moveDirection(newRobot, 'left', board, cnt + 1, moved+[newRobot], minCnt)
    return newRobots

def isAvail(robot, direction, board):
    r = robot[0]
    c = robot[1]
    hv = robot[2]

    if direction == 'up':
        if hv == 0:
            if r-1 >= 0 and board[r-1][c] == 0 and board[r-1][c-1] == 0:
                return True
        elif hv == 1:
            if r-2 >= 0 and board[r-2][c] == 0:
                return True
    elif direction == 'right':
        if hv == 0:
            if c + 1 < len(board) and board[r][c+1] == 0:
                return True
        elif hv == 1:
            if c+1 < len(board) and board[r][c+1] == 0 and board[r-1][c+1] == 0:
                return True
    elif direction == 'down':
        if hv == 0:
            if r+1 < len(board) and board[r+1][c] == 0 and board[r+1][c-1] == 0:
                return True
        elif hv == 1:
            if r+1 < len(board) and board[r+1][c] == 0:
                return True
    elif direction == 'left':
        if hv == 0:
            if c-2 >= 0 and board[r][c-2] == 0:
                return True
        elif hv == 1:
            if c-1 >= 0 and board[r][c-1] == 0 and board[r-1][c-1] == 0:
                return True
    return False

print(solution(	[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))