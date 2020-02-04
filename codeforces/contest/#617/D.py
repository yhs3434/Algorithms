n, a, b, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

cnt = 0
lena = len(arr)
for i in range(lena-1, -1, -1):
    arr[i] %= (a+b)
    if arr[i] == 0:
        arr[i] += (a+b)
    if arr[i] <= a:
        del arr[i]
        cnt += 1
arr.sort()

lena = len(arr)
for i in range(lena):
    arr[i] -= a
    temp = 0
    if arr[i]/a == arr[i]//a:
        temp = arr[i]//a
    else:
        temp = arr[i]//a + 1
    if k - temp >= 0:
        cnt += 1
        k -= temp
    else:
        break
print(cnt)