import math


def maxProfit(A, i, j):
    if i == j:
        return (i, j)
    else:
        mid = math.floor((i + j) / 2)
        left = maxProfit(A, i, mid)
        right = maxProfit(A, mid + 1, j)
        return cross(A, left, right, i, mid + 1, j)


def cross(A, left, right, start, mid, end):
    lowBetween = mid - 1
    highBetween = mid
    for i in range(mid - 1, start -1, -1):
        if (A[i] < A[lowBetween]):
            lowBetween = i
    for i in range(mid, end +1, 1):
        if (A[i] > A[highBetween]):
            highBetween = i
    leftDiff = A[left[1]] - A[left[0]]
    rightDiff = A[right[1]] - A[right[0]]
    betweenDiff = A[highBetween] - A[lowBetween]

    if (betweenDiff > leftDiff and betweenDiff > rightDiff):
        return (lowBetween, highBetween)
    elif (rightDiff > leftDiff and rightDiff > betweenDiff):
        return (right[0], right[1])
    else:
        return (left[0], left[1])


if __name__== "__main__":
    a = [9, 1, 5, 4, 7]
    result = maxProfit(a, 0, len(a) - 1)
    if ((a[result[1]] - a[result[0]]) <= 0):
        print("don't work")
    else:
        print(result)