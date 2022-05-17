import math
def JumpSearch(array, target):
    jump = int(math.sqrt(len(array)))
    for i in range(jump,len(array),jump):
        if array[i] == target:
            return i
        elif array[i] > target:
            begin = i - jump
            for j in range(begin, i):
                if array[j] == target:
                    return j
    for s in range(i, len(array)):
        if array[s] == target:
            return s
    return -1