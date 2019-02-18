import math     

def checkPeak(a, minimum, maximum, size):
    # base case
    if len(a) == 1:
        return a[0]

    # find half
    half = minimum + (maximum - minimum)/2
    half = int(half)

    # use the half spot in the array as the pivot
    pivot = a[half]
    
    #if there are either no neighbors OR the pivot is larger than the left and smaller
    # than the right, we have found our pivot and should return it
    if ((half == 0 or a[half - 1] <= a[half]) and  (half == size - 1 or a[half + 1] <= a[half])): 
        return pivot
    #if there is a left neighbor and the pivot is less than it, must be on the left side
    elif (half > 0 and a[half - 1] > a[half]): 
        return checkPeak(a, minimum, (half - 1), size)
    #if it's not found on the left, it must be found on the right-hand side
    else:
        return checkPeak(a, (half + 1), maximum, size) 

def findPeakInterim(a):
    length = len(a) 
    return checkPeak(a, 0, length - 1, length)


if __name__== "__main__":
    a = [1, 4, 6, 8, 11, 12, 10, 9, 7]
    b = [1, 2, 5, 17, 4, 3]
    c = [1, 17, 5, 4, 3, 2]
    d = [1, 3, 5, 7, 9, 8, 6, 4]
    e = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]

    print(findPeakInterim(a), "is the peak")
    print(findPeakInterim(b), "is the peak")
    print(findPeakInterim(c), "is the peak")
    print(findPeakInterim(d), "is the peak")
    print(findPeakInterim(e), "is the peak")