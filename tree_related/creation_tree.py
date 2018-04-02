class Node:
    """this for creating nodes and manipulating tree """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self

    def __repr__(self):
        return repr(self.data)


def create_tree():
    """ A binary tree """
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    one = Node(1)
    six = Node(6)
    eight = Node(8)
    five = Node(5)
    ten = Node(10)
    three = Node(3)
    four = Node(4)

    two.add_left(seven)
    two.add_right(nine)

    seven.add_left(one)
    seven.add_right(six)

    nine.add_right(eight)

    six.add_right(ten)
    six.add_left(five)

    eight.add_left(three)
    eight.add_right(four)

    print('====Parent======')
    print('Parent of root node 2 ',two.parent)
    print('Parent(2) of child node 7 ',seven.parent)
    print('Parent(8) of child node 3 ',three.parent)

    return two


if __name__ == "__main__":
    print("Running============")
    root = create_tree()
    print("checking root after tree creation")
    print(root)