def quickSort(arr, p, r):
    if(p<r):
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)

def partition(arr, p, r):
    standard = arr[r]
    i = p-1
    for j in range(p, r):
        if(arr[j]<standard):
            i+=1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i+=1
    temp = arr[i]
    arr[i] = arr[r]
    arr[r] = temp
    return i

arr = [10,3,2,5,4,1,7,6,8,9]
print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)