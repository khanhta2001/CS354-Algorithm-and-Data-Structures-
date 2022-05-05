class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Singly_Linked_List:
    def __init__(self, array):
        root = node(array[0])
        self.head = root
        for i in range(1, len(array)):
            root.next = node(array[i])
            root = root.next

    def GetIndex(self, value):
        i = 0
        while self.head is not None:
            if self.head.value == value:
                return i
            i += 1
        return -1

    def Push(self, value):
        while self.head.next is not None:
            self.head = self.head.next
        self.head.next = node(value)

    def Push(self, value, index):
        i = 0
        while self.head.next is not None:
            if i == index:
                break
            self.head = self.head.next

        prev_node = self.head
        medium = node(value)
        con_node = self.head.next
        prev_node.next = medium
        medium.next = con_node

    def Pop(self):
        while self.head.next.next is not None:
            self.head = self.head.next
        popped_node = self.head.next
        self.head.next = popped_node.next
        temp = popped_node.value
        del popped_node
        return temp

    def Pop(self,index):
        i = 0
        while self.head.next.next is not None:
            if i == index:
                break
            self.head = self.head.next
            i += 1
        popped_node = self.head.next
        self.head.next = popped_node.next
        temp = popped_node.value
        del popped_node
        return temp



