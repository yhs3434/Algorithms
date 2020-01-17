strr = input()
arr = []
for i in range(len(strr)):
    arr.append(strr[i:])
arr.sort()
for a in arr:
    print(a)