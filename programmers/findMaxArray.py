def findMaxCrossingSubarray(A, low, mid, high):
    leftSum = -float('inf')
    rightSum = -float('inf')
    sum = 0
    leftMax = 0
    rightMax = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if(sum > leftSum):
            leftSum = sum
            leftMax = i

    sum = 0
    for i in range(mid+1, high+1):
        sum += A[i]
        if(sum > rightSum):
            rightSum = sum
            rightMax = i

    return leftMax, rightMax, leftSum+rightSum

def findMaxSubarray(A, low, high):
    if(low==high):
        return low, high, A[low]
    else:
        mid = int((low+high)/2)
        leftLow, leftHigh, leftMax = findMaxSubarray(A, low, mid)
        rightLow, rightHigh, rightMax = findMaxSubarray(A,mid+1, high)
        crossLow, crossHigh, crossMax = findMaxCrossingSubarray(A, low, mid, high)

        if(leftMax>=rightMax and leftMax>=crossMax):
            return leftLow, leftHigh, leftMax
        elif(rightMax>=leftMax and rightMax>=crossMax):
            return rightLow, rightHigh, rightMax
        else:
            return crossLow, crossHigh, crossMax

probArr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(findMaxSubarray(probArr, 0, len(probArr)-1))