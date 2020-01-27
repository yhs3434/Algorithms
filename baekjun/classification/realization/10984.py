# 내 학점을 구해줘
# https://www.acmicpc.net/problem/10984
# https://github.com/yhs3434/Algorithms

t = int(input())
for xxx in range(t):
    n = int(input())
    totalCredit = 0
    totalGrade = 0
    for yyy in range(n):
        credit, grade = map(float, input().split(' '))
        totalCredit += credit
        totalGrade += credit * grade
    gpa = totalGrade/totalCredit
    print(int(totalCredit), '%.1f'%gpa)