import math

def modifiedMergeSort(A, i, j):
    if (i == j):
        return 0
    else:
        mid = math.floor((i + j) / 2)
        a = modifiedMergeSort(A, i, mid)
        b = modifiedMergeSort(A, mid + 1, j)
        return a + b + merge(A, i, mid + 1, j)

def merge(A, i, mid, j):
    temp = []
    index1 = i
    index2 = mid
    inversions = 0
    while (index1 < mid and index2 <= j):
        if (A[index1] < A[index2]):
            temp.append(A[index1])
            index1+=1
        if (A[index2] < A[index1]):
            temp.append(A[index2])
            index2+=1
            inversions += (mid - index1)
    while (index1 < mid):
        temp.append(A[index1])
        index1 += 1
    while (index2 <= j):
        temp.append(A[index2])
        index2+=1
    for k in range(i, j, 1):
        A[k] = temp[1]
        temp.pop(0)
    return inversions

if __name__== "__main__":
    a = [4, 2, 9, 1, 7]
    result = modifiedMergeSort(a, 0, len(a) - 1)
    print("Number of inversions:", result)