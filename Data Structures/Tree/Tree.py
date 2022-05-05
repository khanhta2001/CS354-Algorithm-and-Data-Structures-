class node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self,dictionary):
        self.parents = list(dictionary.values())
        self.children = list(dictionary.keys())
        self.parents_node = {}
        root = 0
        for i in self.parents:
            if i not in self.children:
                root = i
        self.root_node = node(root)
        hashMap = {self.root_node.value: self.root_node}
        for child in self.children:
            child_node = node(child)
            hashMap[child] = child_node

        for child in self.children:
            child_node = hashMap[child]
            parent = dictionary[child]
            parent_node = hashMap[parent]
            self.parents_node[parent] = parent_node
            parent_node.children.append(child_node)

    def push(self, parent, child):
        if parent in self.parents:
            self.parents_node[parent].children.append(child)
    def pop(self, child, parent = None):
        if parent is None:
            for key in self.parents_node:
                if child in self.parents_node[key].children:
                    self.parents_node[key].children.remove(child)
        else:
            if child in self.parents_node[parent].children:
                self.parents_node[parent].children.remove(child)

    def Print(self):
        looked = [self.root_node]
        while len(looked) != 0:
            string = ""
            count = 0
            for i in looked:
                string += str(i.value) + " "
                count += 1
            print(string)
            while count > 0:
                removed = looked[0]
                for i in removed.children:
                    looked.append(i)
                looked.remove(looked[0])
                count -= 1
