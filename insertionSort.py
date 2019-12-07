def solution(arr):
    for i in range(1, len(arr)):
        curValue = arr[i]
        for j in range(i):
            j =  i-j-1
            if(arr[j] >= curValue):
                arr[j+1] = curValue
                break
            else:
                arr[j + 1] = arr[j]
        if (j==0 and arr[j] == arr[j+1]):
            arr[j] = curValue

    return arr

print(solution([5,2,4,6,1,3,13,9,8,7,12,10,11]))