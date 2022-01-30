from linked_list.singly_linked_list.linked_list import LinkedList


class StackWithLinkedList:
    def __init__(self):
        self.stack = LinkedList([])

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.push(value)
        # print(self)

    def pop(self):
        self.stack.delete(0)
        # print(self)


stack = StackWithLinkedList()
stack.push(1)
print("Stack:", stack)
stack.push(2)
print("Stack:", stack)
stack.push(3)
print("Stack:", stack)
stack.pop()
print("Stack:", stack)
stack.pop()
print("Stack:", stack)