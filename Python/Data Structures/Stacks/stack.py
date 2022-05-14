class Stack:
    def __init__(self,array=None):
        if array is None:
            self.array = []
        else:
            self.array = array

    def push(self, element):
        self.array.append(element)

    def pop(self):
        element = self.array[-1]
        self.array.remove(element)
        return element

    def size(self):
        return len(self.array)

    def peek(self, index):
        return self.array[index]
