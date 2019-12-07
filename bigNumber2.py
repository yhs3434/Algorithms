def solution(numbers):
    num = []
    for n in numbers:
        maxStr = ''.join(num)
        maxNum = num[:]
        for i in range(len(num)+1):
            newNum = num[:i] + [str(n)] + num[i:]
            newStr = ''.join(newNum)
            if(newStr>=maxStr):
                maxStr = newStr
                maxNum = newNum
        num = maxNum
    answer = str(int(''.join(num)))
    return answer


print(solution([0, 0, 0, 0, 0]))