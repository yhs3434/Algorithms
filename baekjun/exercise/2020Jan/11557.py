# Yangjojang of The Year
# https://www.acmicpc.net/problem/11557
# https://github.com/yhs3434

t = int(input())
for xxx in range(t):
    n= int(input())
    schools = []
    for yyy in range(n):
        inp = input().split(' ')
        inp[1] = int(inp[1])
        schools.append(inp)
    schools.sort(key= lambda key: key[1])
    print(schools[-1][0])