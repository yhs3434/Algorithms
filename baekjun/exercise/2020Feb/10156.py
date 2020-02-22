# 과자
# https://www.acmicpc.net/problem/10156
# https://github.com/yhs3434/Algorithms

K, N, M = map(int, input().split(' '))
print(K*N-M) if K*N-M>=0 else print(0)