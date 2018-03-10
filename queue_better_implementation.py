class QueueBetter:
    """
        using head/front and tail/rear concept, we are making O(n)
        dequeue to O(1) ....it is called circular queue
    """

    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            print("Query is full!!!")
            return

        print("Inserting new item:", item)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item


if __name__ == "__main__":
    q = QueueBetter(3)

    q.enqueue("dev")
    print(q.head)
    print(q.tail)
    q.enqueue("-")
    print(q.head)
    print(q.tail)
    q.enqueue("tanvir")
    print(q.head)
    print(q.tail)
    q.enqueue("github")
    print(q.head)
    print(q.tail)

    print("---------")
    while not q.is_empty():
        item = q.dequeue()
        print(item)
        print(q.head)
        print(q.tail)
    print("---------")

    print("after de queue, before adding:",q.items)
    q.enqueue("Python")
    print("after de queue, after adding:",q.items)
    print(q.head)
    print(q.tail)
    # q.enqueue("Python2")
    # print(q.head)
    # q.enqueue("Python3")
    # print(q.head)
    # q.enqueue("Python4")
    # print(q.head)
    # q.dequeue()
    # print(q.head)
    # q.enqueue("Pythonnew")
    # print(q.head)
    # print(q.items)
    # print(q.items[0],"--+--",q.items[1])

    #print(type(q))             # it is a queuebetter object
    #print(type(q.items))       # it is a list!!!!

    print("Head:", q.head)
    print("tail:", q.tail)
