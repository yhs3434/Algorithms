def solution(n):
    answer = 0
    if(n%2==1):
        return answer

    arr = [0, 3, 11]
    for i in range(3, int(n/2)+1):
        arr.append(0)
        arr[i] = arr[i-1]*arr[1]+2
        sum = 0
        for j in range(1,i-1):
            sum += 2*arr[j]
        arr[i] += sum
    answer = arr[int(n/2)]
    print(arr)
    return answer%1000000007

print(solution(100))