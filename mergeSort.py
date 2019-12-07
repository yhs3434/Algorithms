def merge(A, p, q, r):
    leftArr = []
    rightArr = []
    for i in range(p, q+1):
        leftArr.append(A[i])
    for i in range(q+1, r+1):
        rightArr.append(A[i])
    leftArr.append(float('inf'))
    rightArr.append(float('inf'))

    i=0
    j=0
    for k in range(p, r+1):
        if(leftArr[i] <= rightArr[j]):
            A[k] = leftArr[i]
            i += 1
        else:
            A[k] = rightArr[j]
            j += 1

    print(leftArr, rightArr, A)

def merge_sort(A, p, r):
    if (p < r):
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

A = [5,4,3,2,1,6,10,14,23,22,12,11,9,7,8,302,102,112,94,234]

merge_sort(A, 0, len(A)-1)