def getGCD(n, m):
    a, b = n, m
    while n!=m:
        if n>m:
            n = abs(n-m)
        else:
            m = abs(n-m)
    return n