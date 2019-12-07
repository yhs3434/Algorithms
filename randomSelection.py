def randomizedSelection(A, p, r, i):
    if(p==r):
        return A[p]

    q = randomizedPartition(A, p, r)

    k = q - p + 1
    if(i==k):
        return A[q]
    elif(i<k):
        return randomizedSelection(A, p, q-1, i)
    else:
        return randomizedSelection(A, q+1, r, i-k)

def randomizedPartition(A, p, r):
    if(p>=r):
        return p
    stan = A[r]
    i = p
    for j in range(p, r):
        if(A[j]<stan):
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i += 1
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    #randomizedPartition(A, p, i-1)
    #randomizedPartition(A, i+1, r)
    return i

A = [5,4,3,2,7,6,5,10,11,21,9,8,14,23,18]
print(A)
print(randomizedSelection(A, 0, len(A)-1, 3))
print(A)