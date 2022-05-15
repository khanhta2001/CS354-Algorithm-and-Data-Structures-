class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Doubly_Linked_List:
    def __init__(self,array):
        root = node(array[0])
        self.head = root
        for i in range(1, len(array)):
            temp_node = node(array[i])
            root.next = temp_node
            temp_node.prev = root
            root = root.next

    def GetIndex(self,value):
        i = 0
        while self.head is not None:
            if self.head.value == value:
                return i
            i += 1
        return -1

    def PushAtTheEnd(self,value):
        while self.head.next is not None:
            self.head = self.head.next
        self.head.next = node(value)

    def PushAtTheStart(self,value):
        temp_node = node(value)
        temp_node.next = self.head
        self.head.prev = temp_node
        self.head = temp_node

    def Push(self,value,index):
        i = 0
        temp = self.head
        while temp.next is not None:
            if i == index:
                break
            temp = temp.next
            i += 1

        prev_node = temp
        added_node = node(value)
        next_node = temp.next
        prev_node.next = added_node
        added_node.prev = prev_node
        temp.next = next_node
        next_node.prev = temp

    def PopAtTheEnd(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        popped_node = temp.next
        temp.next = popped_node.next
        val = popped_node.value
        del popped_node
        return val

    def PopAtTheStart(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        val = temp.value
        del temp
        return val

    def Pop(self,index):
        temp = self.head
        i = 0
        while i < index - 1:
            temp = temp.next
            i += 1
        popped_node = temp.next
        next_node = popped_node.next
        temp.next = next_node
        next_node.prev = temp
        val = popped_node.value
        del popped_node
        return val

    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
