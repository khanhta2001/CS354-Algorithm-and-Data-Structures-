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
