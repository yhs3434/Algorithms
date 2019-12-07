def countingSort(A):
    k = max(A)
    B = [0 for i in range(len(A))]
    C = [0 for i in range(k+1)]
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(A)):
        i = len(A)-i-1
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B

print(countingSort([2,5,3,0,2,3,0,3]))