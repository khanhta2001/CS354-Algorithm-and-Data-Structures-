def merge(list1, list2):
    list3 = []
    ptr1, ptr2 = 0, 0
    while ptr1 < len(list1) and ptr2 < len(list2):
        if list1[ptr1] < list2[ptr2]:
            list3.append(list1[ptr1])
            ptr1 += 1
        elif list1[ptr1] > list2[ptr2]:
            list3.append(list2[ptr2])
            ptr2 += 1
        else:
            list3.append(list1[ptr1])
            list3.append(list2[ptr2])
            ptr1 += 1
            ptr2 += 1

    for i in range(ptr1, len(list1)):
        list3.append(list1[i])
    for j in range(ptr2, len(list2)):
        list3.append(list2[j])

    return list3


def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = []
    right = []
    for i in range(mid):
        left.append(array[i])
    for j in range(mid, len(array)):
        right.append(array[j])

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)
