def isSorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


def binarysearch(array):
    if isSorted(array) == False:
        pass


