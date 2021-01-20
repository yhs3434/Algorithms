A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))

cnt = 0
val = 0
for i in range(len(arr)-1, -1, -1):
    n = arr[i]
    num = n * (A ** cnt)
    cnt += 1
    val += num

cnt = 0
while True:
    n = B ** cnt
    if n > val:
        break
    cnt += 1
cnt -= 1
answer = []
while cnt >= 0:
    n = B ** cnt
    answer.append(val // n)
    val = val % n
    cnt -= 1

for ans in answer:
    print(ans, end=' ')