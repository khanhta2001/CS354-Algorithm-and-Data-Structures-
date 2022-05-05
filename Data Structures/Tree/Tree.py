class node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self,dictionary=None):
        self.dictionary = dictionary


    def push(self, value):
        self.children.append(value)

    def pop(self, value):
        self.children.remove(value)

