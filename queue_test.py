class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
        # it is of order O(n)
        # cause, pop(0) removes first element and
        # subsequently shifts all other elements to the left
        # 1 step


    def is_empty_list(self):
        if self.items == []:
            return True
        return False

if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)

    while not s.is_empty_list():
        item = s.dequeue()
        print(item)