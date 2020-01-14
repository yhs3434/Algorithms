# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

inp = input()
equation = []
j = 0
for i in range(len(inp)):
    if inp[i] == '+' or inp[i] == '-':
        equation.append(int(inp[j:i]))
        if inp[i] == '+':
            equation.append(1000000)
        else:
            equation.append(1000001)
        j = i+1
equation.append(int(inp[j:]))
nEquation = []
flag = True
sumVal = 0
for i in range(len(equation)):
    cur = equation[i]
    if cur != 1000000 and cur != 1000001:
        sumVal += cur
    if cur == 1000001:
        nEquation.append(sumVal)
        sumVal = 0
nEquation.append(sumVal)
answer = nEquation[0]
for i in range(1,len(nEquation)):
    answer -= nEquation[i]
print(answer)