# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''

    quickSort(numbers, 0, len(numbers)-1)

    numbers.reverse()
    for n in numbers:
        answer+=str(n)

    answer = str(int(answer))

    return answer

def compare2(x,y):
    str_x = str(x)
    str_y = str(y)

    if((str_x+str_y)>(str_y+str_x)):
        return -1
    elif((str_x+str_y)<(str_y+str_x)):
        return 1
    else:
        return 0

def quickSort(arr, bot, top):
    if(bot>=top):
        return
    fivot = arr[top]
    i=bot-1
    j=bot

    while i<top:
        i+=1
        if(compare2(arr[i], fivot)==1):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    quickSort(arr, bot, j-1)
    quickSort(arr, j+1, top)

print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0,0]))
solution([6, 10, 2])