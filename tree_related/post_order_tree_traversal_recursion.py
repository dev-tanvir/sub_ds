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


def post_order(node):

    if node.left:
        post_order(node.left)

    if node.right:
        post_order(node.right)

    print(node)


if __name__ == "__main__":
    root = create_tree()
    print(root)
    print('Post order binary tree traversing===')
    post_order(root)