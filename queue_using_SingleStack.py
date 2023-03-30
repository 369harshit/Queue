class Stack:
    def __init__(self):
        self.q = Queue()

    def empty(self):
        print(self.q.empty())

    def push(self, data):
        self.q.enqueue(data)
        print(data, "is pushed")

    def pop(self):
        for i in range(self.q.get_size() - 1):
            dequeued = self.q.dequeue()  # Dequeuing
            self.q.enqueue(dequeued)  # again enqueueing it so that last element reaches front of queue
        print("{} is popped".format(self.q.dequeue()))  # Dequeueing now removes the recently added element

    def size(self):
        print("{} is the size of stack".format(self.q.get_size()))

    def top(self):
        if not self.q.empty():
            print("{} is top element of stack".format(self.q.top()))
        else:
            print("Stack Empty!!!")


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def top(self):
        return self.items[-1]

    def empty(self):
        return self.items == []

    def enqueue(self, data):
        self.size += 1
        self.items.append(data)

    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)

    def get_size(self):
        return self.size


s = Stack()

s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

s.pop()
s.pop()
s.empty()
s.size()
s.top()