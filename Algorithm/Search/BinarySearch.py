def isSorted(array):
    # check if the list is sorted or not
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def Sort(array):
    # sort the list using quicksort
    quicksort(array, 0, len(array)-1)


def BinarySearch(array, target):
    # run binary search
    low = 0
    high = len(array)
    while low <= high:
        mid = low + (high-low)//2

        # check if the middle element equals, smaller, or larger than the target
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    #if not found, return -1
    return -1

def BinarySearch_Helper(array, target):
    if isSorted(array):
        return BinarySearch(array, target)
    Sort(array)
    return BinarySearch(array, target)



def partition(array, low, high):
    pivot = array[high]
    pos = low - 1

    # traverse through all elements
    # compare each element with the pivot
    for j in range(low, high):
        if array[j] < pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by pos
            pos += 1
            element = array[pos]
            array[pos] = array[j]
            array[j] = element

    # return the position from where the partition is done
    return pos + 1


def quicksort(array, low, high):
    if low < high:
        # find the pivot element such that
        # element smaller than pivot are on the left
        # element larger than pivot are on the right
        pivot = partition(array, low, high)

        # recursive call on the left of the pivot
        quicksort(array, low, pivot - 1)

        # recursive call on the right of the pivot
        quicksort(array, pivot + 1, high)

