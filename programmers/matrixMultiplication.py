# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]
    arr2 = convertRC(arr2)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            raw1 = arr1[i]
            raw2 = arr2[j]
            newRaw = [raw1[i]*raw2[i] for i in range(len(raw1))]
            answer[i][j] = sum(newRaw)

    return answer

def convertRC(arr):
    newArr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
    return newArr

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))