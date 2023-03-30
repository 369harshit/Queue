class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating a Queue class to implement the queue.


class Queue:
    # constructor, initializing both front and rear to None.
    # As there is no element present in the queue.
    def __init__(self):
        self.front = None
        self.rear = None

    # method to check if the queue is empty or not.

    def empty(self):
        return self.front is None

    # method to add an element into the queue.

    def enqueue(self, item):
        temp = QueueNode(item)

        # checking if there is any element present or not.
        if self.rear is None:
            self.front = temp
            self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp

    # method to remove an element from the queue.

    def dequeue(self):

        # checking if the queue is empty.
        # if the queue is empty, we cannot remove any element.
        if self.empty():
            return

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print("Queue's current front " + str(queue.front.data))
    print("Queue's current rear " + str(queue.rear.data))

    queue.dequeue()
    queue.dequeue()

    print("Queue's current front " + str(queue.front.data))
    print("Queue's current rear " + str(queue.rear.data))
