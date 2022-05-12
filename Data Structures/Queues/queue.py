class Queue:
    def __init__(self, array=None):
        if array is None:
            self.array = []
        else:
            self.array = array

    def enqueue(self, element):
        self.array.append(element)

    def dequeue(self):
        first_element = self.array[0]
        self.array.remove(first_element)
        return first_element

    def size(self):
        return len(self.array)

    def peek(self, index):
        return self.array[index]
