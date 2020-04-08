import sys

def solution(k, room_number):
    answer = []

    rooms2 = {}

    
    for num in room_number:
        if num not in rooms2:
            answer.append(num)
            rooms2[num] = num + 1
        else:
            cur = num
            visited = []
            while cur in rooms2:
                visited.append(cur)
                cur = rooms2[cur]
            answer.append(cur)
            rooms2[cur] = cur + 1
            for vNum in visited:
                rooms2[vNum] = rooms2[cur]
    return answer

print(solution(10, [1,3,4,1,3,1]))
