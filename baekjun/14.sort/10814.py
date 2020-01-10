# 나이순 정렬
# https://www.acmicpc.net/problem/10814

n = int(input())
people = []
for xxx in range(n):
    person = input().split(' ')
    person[0] = int(person[0])
    people.append(person)
people.sort(key=lambda key: key[0])
for person in people:
    print(person[0], person[1])