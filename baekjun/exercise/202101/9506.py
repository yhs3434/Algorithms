while True:
    n = int(input())
    if n == -1:
        break

    sumVal = 0
    answer = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sumVal += i
            answer.append(i)
    if sumVal == n:
        print(n,'=',end=' ')
        for i in range(len(answer)):
            ans = answer[i]
            if i < len(answer) - 1:
                print(ans, end=' + ')
            else:
                print(ans)
    else:
        print(n, 'is NOT perfect.')