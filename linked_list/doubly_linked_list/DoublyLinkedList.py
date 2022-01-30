import cur as cur

from linked_list.doubly_linked_list.Node import Node


class DoublyLinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        self.length = 0
        if lst is not None:
            for val in lst:
                self.push(val)
        print("Doubly Linked List Initialized With List:", str(lst))
        print("After:", self)

    def __str__(self):
        if self.head is None and self.tail is None:
            return ""
        else:
            values = []
            curr = self.head
            while curr:
                values.append(curr.value)
                curr = curr.next
            return " <-> ".join(str(val) for val in values)

    def push(self, value):
        if not value:
            return
        print("-----------------------------------")
        print("Pushing to List", value)
        print("BEFORE: ", self)

        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.length += 1
        print("Pushed to List", value)
        print("After: ", self)
        print("-----------------------------------\n\n")

    def insert(self, value, location):
        if self.head is None:
            self.push(value)
            return

        print("-----------------------------------")
        print("Inserting into List", value, location)
        print("BEFORE: ", self)
        newNode = Node(value)

        if location == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        elif location == -1 or location == self.length - 1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            curr = self.head
            index = 0

            while index < location - 1 and curr:
                curr = curr.next
                index += 1

            if curr:
                newNode.next = curr.next
                newNode.prev = curr
                curr.next.prev = newNode
                curr.next = newNode



        self.length += 1
        print("Inserted to List", value)
        print("After: ", self)
        print("-----------------------------------\n\n")

    def delete(self, location):
        if not (-1 <= location < self.length):
            return

        print("-----------------------------------")
        print("Delete from List", location)
        print("BEFORE: ", self)
        toDelete = None

        if location == 0:
            toDelete = self.head
            self.head = toDelete.next
            self.head.prev = None
        elif location == -1 or location == self.length - 1:
            toDelete = self.tail
            self.tail = toDelete.prev
            self.tail.next = None
        else:
            curr = self.head
            index = 0

            while index < location - 1 and curr:
                curr = curr.next
                index += 1

            if curr:
                toDelete = curr.next
                curr.next = toDelete.next
                toDelete.next.prev = curr

        self.length -= 1
        value = toDelete.value
        toDelete = None
        print("Deleted from List", value)
        print("After: ", self)
        print("-----------------------------------\n\n")
        return value


if __name__ == '__main__':
    lst = DoublyLinkedList([1, 2, 3, 4])
    lst.insert(50, 0)
    lst.insert(60, -1)
    lst.insert(70, 3)
    print("Deleted", lst.delete(3))
    print("Deleted", lst.delete(0))
    print("Deleted", lst.delete(-1))
