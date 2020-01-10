def mergeSort(a):
    # used more than once, just find it here
    arrLength = len(a)
    # the base case
    if(arrLength > 1):
        # find the mid
        mid = arrLength//2
        # split the arrays into two
        a1 = a[:mid]
        a2 = a[mid:]
        # mergesort the two split arrays
        mergeSort(a1)
        mergeSort(a2)

        #lengths are used more than once
        len1 = len(a1)
        len2 = len(a2)

        i = j = k = 0
        #copy data to different arrays
        while i < len1 and j < len2:
            if a1[i] < a2[j]:
                a[k] = a1[i]
                i+=1
            else:
                a[k] = a2[j]
                j+=1
            k+=1
        
        #make sure arrays are both empty
        while i < len1:
            a[k] = a1[i]
            i+=1
            k+=1
        while j < len2:
            a[k] = a2[j]
            j+=1
            k+=1

#driver stuff
if __name__ == '__main__': 
    # test array
    a = [1, 5, 9, 3, 7, 12, 15, 8, 21]
    # spots to search for
    spots = [2, 5, 7]
    # sort the arrays
    mergeSort(a)

    valNum = 0
    for val in spots:
        print(val, '-th value is', a[val - 1])



    