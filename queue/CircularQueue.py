#
#  Created By: Mohinish Joshi on 30/01/22, 6:13 PM
#

class CircularQueue:
    def __init__(self, max_size):
        self.start = -1
        self.top = -1
        self.queue = max_size * [None]
        self.maxSize = max_size

    def __str__(self):
        return ", ".join([str(x) for x in self.queue])

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top == self.maxSize - 1:
            return True
        else:
            return False

    def isEmpty(self):
        return self.top == -1

    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.top + 1 == self.maxSize:
                # We are at the end of the queue
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.queue[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            oldStart = self.start
            firstElement = self.queue[self.start]
            if self.start + 1 == self.maxSize:
                self.queue[self.start] = None
            elif self.start == self.top:
                self.start = -1
                self.top = -1
            else:
                self.start += 1
            self.queue[oldStart] = None
            return oldStart


queue = CircularQueue(3)
print("Queue", queue)
queue.enqueue(1)
print("Queue", queue)
queue.enqueue(2)
print("Queue", queue)
queue.enqueue(3)
print("Queue:", queue)
queue.dequeue()
print("Queue:", queue)
queue.dequeue()
print("Queue:", queue)
# print("Peek", queue.peek())

