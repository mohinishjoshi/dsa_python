from linked_list.node import Node


class LinkedList:
    # def __init__(self):
    #     print("__init")
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

    def __init__(self, lst):
        self.head = None
        self.tail = None
        self.length = 0
        for val in lst:
            self.append(val)

    def __str__(self):
        curr = self.head
        value = ""
        while curr is not None:
            value += str(curr.value) + ", "
            curr = curr.next
        return value.strip(", ")

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        if self.tail is None:
            self.tail = self.head

    def append(self, value):
        node = Node(value)
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length +=1

    def pop(self):
        assert self.length > 0 and self.tail is not None, "The linked List is empty"

        curr = self.head
        while curr.next is not self.tail:
            curr = curr.next

        to_delete = self.tail
        self.tail = curr
        self.tail.next = None
        self.length -= 1
        del to_delete


lst = LinkedList([1,2,3,4])
print(lst)
lst.push(5)
print(lst)
lst.pop()
print(lst)
lst.append(5)
print(lst)
