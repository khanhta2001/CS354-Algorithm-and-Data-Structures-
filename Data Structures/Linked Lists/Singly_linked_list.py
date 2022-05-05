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
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return i
            temp = temp.next
            i += 1
        return -1

    def Push(self, value):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node(value)

    def PushIndex(self, value, index):
        i = 0
        temp = self.head
        while i < index - 1:
            temp = temp.next
            i += 1
        prev_node = temp
        medium = node(value)
        con_node = temp.next
        prev_node.next = medium
        medium.next = con_node

    def Pop(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        popped_node = temp.next
        temp.next = popped_node.next
        val = popped_node.value
        del popped_node
        return val

    def PopIndex(self,index):
        i = 0
        temp = self.head
        while i < index-1:
            temp = temp.next
            i += 1
        popped_node = temp.next
        temp.next = popped_node.next
        val = popped_node.value
        del popped_node
        return val

    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


