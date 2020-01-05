# 회의실 배정
# https://www.acmicpc.net/problem/1931

N = int(input())
meetings = []
for i in range(N):
    meet = list(input().split(' '))
    meet = list(map(int, meet))
    meetings.append(meet)

answer = 0
delim = 0
meetings.sort(key=lambda key:key[0])
meetings.sort(key=lambda key:key[1])
for meeting in meetings:
    if(meeting[0]>=delim):
        answer += 1
        delim = meeting[1]
print(answer)