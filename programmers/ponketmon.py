# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0

    N = len(nums)//2
    nums = list(set(nums))
    answer = N if N<len(nums) else len(nums)

    return answer

print(solution([3,3,3,2,2,2]))