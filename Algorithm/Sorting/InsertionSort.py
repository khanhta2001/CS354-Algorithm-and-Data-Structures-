def insertionsort(array):
    minimum = 99999999999
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                medium = array[i]
                array[i] = array[j]
                array[j] = medium
    return array


