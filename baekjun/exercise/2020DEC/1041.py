N = int(input())
arr = list(map(int, input().split()))

answer = 0

vol1 = min(arr)

avails = set()
for i in range(6):
    for j in range(i+1, 6):
        if (i==0 and j==5) or (i==1 and j==4) or (i==2 and j==3):
            continue
        avails.add(arr[i]+arr[j])
vol2 = min(avails)

avails = set()
avails.add(arr[0]+arr[1]+arr[2])
avails.add(arr[0]+arr[2]+arr[4])
avails.add(arr[0]+arr[3]+arr[4])
avails.add(arr[0]+arr[1]+arr[3])
avails.add(arr[5]+arr[1]+arr[2])
avails.add(arr[5]+arr[2]+arr[4])
avails.add(arr[5]+arr[3]+arr[4])
avails.add(arr[5]+arr[1]+arr[3])
vol3 = min(avails)


if N == 1:
    answer = sum(arr) - max(arr)
else:
    answer += vol3*4
    answer += vol2*4*(N-2)
    answer += vol2*4*(N-1)
    n = N-1
    answer += vol1*(5*(n**2) - 6*n + 1)
print(answer)