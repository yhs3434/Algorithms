# 평균 점수
# https://www.acmicpc.net/problem/10039
# https://github.com/yhs3434

vals = []
for xxx in range(5):
    val = int(input())
    if val < 40:
        val = 40
    vals.append(val)
print(sum(vals)//5)