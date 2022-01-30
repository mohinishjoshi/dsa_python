#
#  Created By: Mohinish Joshi on 30/01/22, 6:00 PM
#

class QueueWithArray:
    def __init__(self, *elements):
        self.queue = []

    def __str__(self):
        if len(self.queue) == 0:
            return "Queue Empty"
        else:
            return " -> ".join([str(x) for x in self.queue])

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return
        else:
            return self.queue.pop(0)

    def peek(self):
        return self.queue[0]


queue = QueueWithArray()
print("Queue", queue)
queue.enqueue(1)
print("Queue", queue)
queue.enqueue(2)
print("Queue", queue)
queue.enqueue(3)
print("Queue", queue)
queue.dequeue()
print("Queue", queue)
queue.dequeue()
print("Queue", queue)
print("Peek", queue.peek())

