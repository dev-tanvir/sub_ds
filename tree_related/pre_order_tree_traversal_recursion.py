class Node:
    """this for creating nodes and manipulating tree """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

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

    return two


def pre_order(node):
    print(node)

    if node.left:
        pre_order(node.left)

    if node.right:
        pre_order(node.right)


if __name__ == "__main__":
    root = create_tree()
    print(root)
    print('Pre order binary tree traversing===')
    pre_order(root)