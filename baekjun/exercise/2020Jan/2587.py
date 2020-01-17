# 대표값2
# https://www.acmicpc.net/problem/2587

nums = []
for i in range(5):
    nums.append(int(input()))
nums.sort()
print(sum(nums)//5)
print(nums[2])