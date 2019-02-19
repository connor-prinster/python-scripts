import random
import math

Results = []

def findKths(A, K): 
    #if array of numbers and array of positions aren't empty
    if (A != [] and K != []):
        # pivot = median
        pivot = math.floor(len(A) / 2)
        # for splitting the array
        A1 = []
        A2 = []
        # putting the values in arrays based on pivots
        for i in A:
            if i < A[pivot]:
                A1.append(i)
            if i > A[pivot]:
                A2.append(i)
        # for seeing which ks need to go in which k1, k2
        position = len(A1) + 1
        # set up two arrays for splitting array of k's
        K1 = []
        K2 = []
        # make k into nothing for now
        k = None
        # put the k-th choices into sub-arrays so we don't
        # look for the i-th value if the size of the subarray
        # can't even contain that.
        for i in K:
            if i < position:
                K1.append(i)
            if i > position:
                K2.append(i - position)
            if i == position:
                k = i
        # if k no longer equals none
        if k != None:
            # the pivot is one of the positions we needed!
            Results.append(A[pivot])
        # do the stuff on both left and right
        findKths(A1, K1)
        findKths(A2, K2)


if __name__ == "__main__":
    a = [1, 5, 9, 3, 7, 12, 15, 8, 21]
    k = [2, 5, 7]   
    findKths(a, k)
    print(Results)