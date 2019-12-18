def solution(arr):
    answer = 0

    p = [arr[i][0] for i in range(len(arr))]
    p.append(arr[-1][1])
    length = len(p)
    print(p)

    m = [[0 for i in range(length)] for j in range(length)]
    s = [[0 for i in range(length)] for j in range(length)]

    for l in range(2, length):
        for i in range(1, length-l+1):
            j = i+l-1
            q = float('inf')
            for k in range(i, j):
                val = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if (val < q):
                    q = val
                    m[i][j] = val
                    s[i][j] = k

    printOptimal(s, 1, length-1)

    return

def printOptimal(s, left, right):
    if(left==right):
        print('A'+str(left), end=' ')
    else:
        print('(', end=' ')
        printOptimal(s, left, s[left][right])
        printOptimal(s, s[left][right]+1, right)
        print(')', end=' ')

solution([[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]])