class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):                    # this to print our linked list
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ",".join(nodes)


    def prepend(self):
        pass

    def append(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def search(self):
        pass
