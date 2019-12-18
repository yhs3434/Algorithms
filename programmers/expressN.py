# N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = -1
    arr = [None]
    for i in range(1, 9):
        arr.append([int(str(N)*(i))])
        for j in range(1, i):
            calculate(arr[j], arr[i-j], arr[i])
        if number in arr[i]:
            answer = i
            break

    return answer

def calculate(a, b, arr):
    hash = {}
    for i in a:
        for j in b:
            hash[i+j] = True
            hash[i*j] = True
            hash[i-j] = True
            if(j != 0):
                hash[i//j] = True
    for key in hash:
        arr.append(key)

print(solution(5, 12))