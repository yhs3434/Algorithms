while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a == b == c:
        print('Equilateral')
    elif (b+c) <= a or (a+c) <= b or (a+b) <= c:
        print('Invalid')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')