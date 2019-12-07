def solution(n):
    answer = 0

    exp = largestNumber(n)
    n2 = makeTwo(n, exp)
    count_1 = n2.count('1')

    nextN = n
    while(True):
        nextN += 1
        exp = largestNumber(nextN)
        n22 = makeTwo(nextN, exp)
        count_11 = n22.count('1')
        if(count_1 == count_11):
            break
    answer = nextN
    return answer

def largestNumber(n):
    count = 0
    delim = 1
    while(True):
        if (n//delim>=1):
            count+=1
            delim*=2
        else:
            break
    return count-1

def makeTwo(n, exp):
    str = ""
    num = n
    val = 2**exp
    while(val>=1):
        if(num//val>=1):
            str += "1"
        else:
            str += "0"
        num=num%val
        val = val//2
    return str

print(solution(78))