# 덩치
# https://www.acmicpc.net/problem/7568

def solution(people):
    answer = [0 for i in range(len(people))]

    for i in range(len(people)):
        p = people[i]
        for j in range(len(people)):
            if comparePerson(people[j], p):
                answer[i] += 1
        answer[i] += 1

    return answer

def comparePerson(x, y):
    if x[0] > y[0] and x[1] > y[1]:
        return True
    return False

n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().split(' '))))
answer = solution(people)
for a in answer:
    print(a, end = ' ')