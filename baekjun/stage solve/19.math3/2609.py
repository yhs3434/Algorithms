# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

def getGCD(n, m):
    a, b = n, m
    while n!=m:
        if n>m:
            n = abs(n-m)
        else:
            m = abs(n-m)
    return n

a, b = map(int, input().split(' '))
gcd = getGCD(a, b)
lcm = gcd*(a//gcd)*(b//gcd)
print(gcd)
print(lcm)