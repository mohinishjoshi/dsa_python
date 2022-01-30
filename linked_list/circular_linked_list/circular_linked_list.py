from linked_list.Node import Node


class CircularLinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        self.length = 0
        if lst is not None and len(lst) > 0:
            for value in lst:
                self.push(value)

    def __str__(self):
        if self.head is None or self.tail is None:
            return ""
        curr = self.head
        values = []
        while True:
            values.append(curr.value)
            curr = curr.next
            if curr == self.head:
                break
        if len(values) > 0:
            return " -> ".join([str(val) for val in values])
        else:
            return ""

    def push(self, value):
        assert value is not None, "Value is required"

        print("-----------------------------------")
        print("Pushing to List", value)
        print("BEFORE: ", self)
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        
        self.length +=1
        print("Pushed to List", value)
        print("After: ", self)
        print("-----------------------------------\n\n")

    def insert(self, value, location=0):
        assert value is not None, "Value should be valid"
        assert location >= -1, "Location should be > -1"
        newNode = Node(value)
        print("-----------------------------------")
        print("Inserting into List", value, location)
        print("BEFORE: ", self)

        if self.head is None:
            # head - "NewNode"
            # tail -   ^
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
            self.length += 1
            print("Head is None, inserted at start", value, location)
            print("After: ", self)
            print("-----------------------------------\n\n")
            return

        if location == 0:
            #            ___________________
            #        new/    (old)X         \
            # head - "NewNode" -> 2 -> 3 -> 4
            #                                \___tail
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode
            self.length += 1
        elif location == -1:
            self.push(value)
        else:
            curr = self.head.next
            index = 1
            while index < location - 1 and curr.next is not self.head:
                index += 1
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
            self.length += 1
            if self.tail.next is newNode:
                self.tail = newNode
        print("Pushed to List", value)
        print("After: ", self)
        print("-----------------------------------\n\n")

    def delete(self, location):
        assert self.head is not None and self.tail is not None, "List is empty"
        assert self.length > 0, "List is empty"
        assert location >= -1, "Location should be > -1"
        deletedNode = None
        print("-----------------------------------")
        print("Deleting from List", location)
        print("BEFORE: ", self)
        if self.head == self.tail:
            deletedNode = self.head
            self.tail.next = None
            self.tail = None
            self.head = None
            self.length -= 1
        if location == 0:
            #             Only 1 element in List
            deletedNode = self.head
            self.head = self.head.next
            self.tail.next = self.head
        elif location == -1 or location == self.length - 1:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            deletedNode = curr.next
            curr.next = deletedNode.next
            self.tail = curr
        else:
            curr = self.head.next
            index = 1
            while index < location - 1 and curr.next != self.tail.next:
                index += 1
                curr = curr.next
            deletedNode = curr.next
            curr.next = deletedNode.next
            # if deletedNode.next == self.head:
            #     self.tail = curr

        deletedNode.next = None
        val = deletedNode.value
        deletedNode = None
        self.length -= 1
        print("Deleted at location: ", location)
        print("After: ", self)
        print("-----------------------------------\n\n")
        return val

    def indexOf(self, value):
        if self.length == 0 or self.head is None:
            return -1
        else:
            curr = self.head
            index = 0
            while curr:
                if curr.value == value:
                    return index
                curr = curr.next
                index += 1
                if curr.next == self.head:
                    break

            if curr is not None and curr.value == value:
                return index
            else:
                return -1

    def deleteList(self):
        self.head = None
        self.tail = None
        self.length = 0



if __name__ == '__main__':
    lst = CircularLinkedList([1, 2, 3, 4])
    lst.insert(50, 0)
    lst.insert(60, -1)
    lst.insert(70, 3)
    lst.insert(80, 9)
    print("deleted:", lst.delete(0))
    print("deleted:", lst.delete(3))
    print("deleted:", lst.delete(-1))
    print("Index of 70", lst.indexOf(70))
    lst.deleteList()
