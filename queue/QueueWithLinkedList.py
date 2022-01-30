#
#  Created By: Mohinish Joshi on 30/01/22, 6:00 PM
#
from linked_list.singly_linked_list.linked_list import LinkedList


class QueueWithLinkedList:
    def __init__(self, *elements):
        self.queue = LinkedList(elements)

    def __str__(self):
        return str(self.queue)

    def isEmpty(self):
        return self.queue.length == 0

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return
        else:
            self.queue.delete(0)

    def peek(self):
        return self.queue.head.value


# Uncomment to Run
# queue = QueueWithLinkedList()
# print("Queue", queue)
# queue.enqueue(1)
# print("Queue", queue)
# queue.enqueue(2)
# print("Queue", queue)
# queue.enqueue(3)
# print("Queue", queue)
# queue.dequeue()
# print("Queue", queue)
# queue.dequeue()
# print("Queue", queue)
# print("Peek", queue.peek())

